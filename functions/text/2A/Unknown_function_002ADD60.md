# sub_002ADD60

- RVA: `0x002ADD60`–`0x002ADD7F` (길이 `31` bytes)
- VA: `0x00000001402ADD60`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006D3B0`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002ADD63` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002ADD6A` → [sub_002ADE02](Unknown_function_002ADE02.md) (`tail-transfer`)
  - `0x002ADD7A` → [sub_002ADB1C + 0x5B](Unknown_function_002ADB1C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002ADD60  41 FF C7                        inc r15d
002ADD63  44 85 3D 42 75 D1 00            test dword ptr [rip + 0xd17542], r15d
002ADD6A  0F 84 92 00 00 00               je 0x1402ade02
002ADD70  F3 90                           pause
002ADD72  48 8B 1E                        mov rbx, qword ptr [rsi]
002ADD75  48 85 DF                        test rdi, rbx
002ADD78  75 E6                           jne 0x1402add60
002ADD7A  E9 F8 FD FF FF                  jmp 0x1402adb77
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002ADD60(void)
{
    __int64 v_r15;

    v_r15 = (unsigned int)((v_r15) + 1);
    if (((v_rdi) & (*(unsigned __int64 *)(v_rsi))) != 0) goto loc_002ADD60;
}
```

## 5. (Beta) C Style

```c
void sub_002ADD60(void)
{
    int64_t local_r15;

    local_r15 = (uint32_t)((local_r15) + 1);
    if (((local_rdi) & (*(uint64_t *)(local_rsi))) != 0) goto loc_002ADD60;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002ADD60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002ADD60[BB_002ADD60]
  bb_002ADD70[BB_002ADD70]
  bb_002ADD7A[BB_002ADD7A]
  bb_002ADD60 -->|fallthrough| bb_002ADD70
  bb_002ADD70 -->|branch| bb_002ADD60
  bb_002ADD70 -->|fallthrough| bb_002ADD7A
```
