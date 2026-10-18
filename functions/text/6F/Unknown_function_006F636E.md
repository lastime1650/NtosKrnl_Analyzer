# sub_006F636E

- RVA: `0x006F636E`–`0x006F6399` (길이 `43` bytes)
- VA: `0x00000001406F636E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B0C20`
- 디코드: `11`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006F6383` → [CcIsThereDirtyData + 0x79](../48/CcIsThereDirtyData_function_0048BE30.md) (`tail-transfer`)
  - `0x006F6394` → [CcIsThereDirtyData + 0x7C](../48/CcIsThereDirtyData_function_0048BE30.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F636E  48 8D 48 01                     lea rcx, [rax + 1]
006F6372  48 83 F9 01                     cmp rcx, 1
006F6376  76 10                           jbe 0x1406f6388
006F6378  F0 48 0F B1 8F 10 05 00 00      lock cmpxchg qword ptr [rdi + 0x510], rcx
006F6381  75 EB                           jne 0x1406f636e
006F6383  E9 21 5B D9 FF                  jmp 0x14048bea9
006F6388  74 07                           je 0x1406f6391
006F638A  B9 0E 00 00 00                  mov ecx, 0xe
006F638F  CD 29                           int 0x29
006F6391  40 32 F6                        xor sil, sil
006F6394  E9 13 5B D9 FF                  jmp 0x14048beac
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_006F636E(void)
{
    __int64 v_rsi;

    if ((result + 1) <= 1) goto loc_006F6388;
    if ((result + 1) != 1) goto loc_006F636E;
loc_006F6388:
    if ((result + 1) != 1) {
        a1 = 14;
    }
    v_rsi = 0;
}
```

## 5. (Beta) C Style

```c
void sub_006F636E(void)
{
    int64_t local_rsi;

    if ((result + 1) <= 1) goto loc_006F6388;
    if ((result + 1) != 1) goto loc_006F636E;
loc_006F6388:
    if ((result + 1) != 1) {
        a1 = 14;
    }
    local_rsi = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F636E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F636E[BB_006F636E]
  bb_006F6378[BB_006F6378]
  bb_006F6383[BB_006F6383]
  bb_006F6388[BB_006F6388]
  bb_006F638A[BB_006F638A]
  bb_006F6391[BB_006F6391]
  bb_006F636E -->|branch| bb_006F6388
  bb_006F636E -->|fallthrough| bb_006F6378
  bb_006F6378 -->|branch| bb_006F636E
  bb_006F6378 -->|fallthrough| bb_006F6383
  bb_006F6388 -->|branch| bb_006F6391
  bb_006F6388 -->|fallthrough| bb_006F638A
  bb_006F638A -->|flow| bb_006F6391
```
