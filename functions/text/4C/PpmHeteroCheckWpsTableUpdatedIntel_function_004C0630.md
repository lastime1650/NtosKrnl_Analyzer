# PpmHeteroCheckWpsTableUpdatedIntel

- RVA: `0x004C0630`–`0x004C0658` (길이 `40` bytes)
- VA: `0x00000001404C0630`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004C0632` → RVA `0x00FC6A94` (`ALMOSTRO`; read)
- `0x004C063A` → RVA `0x00FC5003` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C0630  32 C0                           xor al, al
004C0632  38 05 5C 64 B0 00               cmp byte ptr [rip + 0xb0645c], al
004C0638  74 1C                           je 0x1404c0656
004C063A  80 3D C2 49 B0 00 02            cmp byte ptr [rip + 0xb049c2], 2
004C0641  75 13                           jne 0x1404c0656
004C0643  B9 B1 01 00 00                  mov ecx, 0x1b1
004C0648  0F 32                           rdmsr
004C064A  48 C1 E2 20                     shl rdx, 0x20
004C064E  48 0B C2                        or rax, rdx
004C0651  C1 E8 1A                        shr eax, 0x1a
004C0654  24 01                           and al, 1
004C0656  C3                              ret
004C0657  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmHeteroCheckWpsTableUpdatedIntel(__int64 a1, __int64 a2)
{
    __int64 result;

    result = 0;
    if ((*(unsigned __int8 *)(v_rip + 11560028)) == 0) goto loc_004C0656;
    if ((*(unsigned __int8 *)(v_rip + 11553218)) == 2) {
        a1 = 433;
        a2 = (a2) << (32);
        result = (result) | (a2);
        result = (unsigned int)((result) >> (26));
        result = (unsigned __int8)((result) & (1));
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmHeteroCheckWpsTableUpdatedIntel(int64_t Arg1, int64_t Arg2)
{
    int64_t result;

    result = 0;
    if ((*(uint8_t *)(v_rip + 0xB0645C)) == 0) goto loc_004C0656;
    if ((*(uint8_t *)(v_rip + 0xB049C2)) == 2) {
        Arg1 = 433;
        Arg2 = (Arg2) << (32);
        result = (result) | (Arg2);
        result = (uint32_t)((result) >> (26));
        result = (uint8_t)((result) & (1));
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C0630&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C0630[BB_004C0630]
  bb_004C063A[BB_004C063A]
  bb_004C0643[BB_004C0643]
  bb_004C0656[BB_004C0656]
  bb_004C0657[BB_004C0657]
  bb_004C0630 -->|branch| bb_004C0656
  bb_004C0630 -->|fallthrough| bb_004C063A
  bb_004C063A -->|branch| bb_004C0656
  bb_004C063A -->|fallthrough| bb_004C0643
  bb_004C0643 -->|flow| bb_004C0656
```
