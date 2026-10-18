# PpmHeteroGetHgsPlusParkingEnablementStatus

- RVA: `0x004B2680`–`0x004B26A4` (길이 `36` bytes)
- VA: `0x00000001404B2680`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `12`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopInitializeHeteroProcessors](../../page/A5/PopInitializeHeteroProcessors_function_00A53570.md) at `0x00A538B3`

### Static image references
- `0x004B2682` → RVA `0x00FC6B40` (`ALMOSTRO`; read)
- `0x004B268F` → RVA `0x00FC6A96` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B2680  32 C9                           xor cl, cl
004B2682  83 3D B7 44 B1 00 05            cmp dword ptr [rip + 0xb144b7], 5
004B2689  74 04                           je 0x1404b268f
004B268B  8A C1                           mov al, cl
004B268D  C3                              ret
004B268E  CC                              int3
004B268F  38 0D 01 44 B1 00               cmp byte ptr [rip + 0xb14401], cl
004B2695  BA 01 00 00 00                  mov edx, 1
004B269A  0F B6 C1                        movzx eax, cl
004B269D  0F 45 C2                        cmovne eax, edx
004B26A0  8A C8                           mov cl, al
004B26A2  EB E7                           jmp 0x1404b268b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmHeteroGetHgsPlusParkingEnablementStatus(unsigned __int8 a1)
{
    __int64 result;

    a1 = 0;
    if ((*(unsigned int *)(v_rip + 11617463)) == 5) goto loc_004B268F;
loc_004B268B:
    return 0;
loc_004B268F:
    result = 0;
    if ((*(unsigned __int8 *)(v_rip + 11617281)) != 0) { result = 1; }
    goto loc_004B268B;
}
```

## 5. (Beta) C Style

```c
int64_t PpmHeteroGetHgsPlusParkingEnablementStatus(uint8_t Arg1)
{
    int64_t result;

    Arg1 = 0;
    if ((*(uint32_t *)(v_rip + 0xB144B7)) == 5) goto loc_004B268F;
loc_004B268B:
    return 0;
loc_004B268F:
    result = 0;
    if ((*(uint8_t *)(v_rip + 0xB14401)) != 0) { result = 1; }
    goto loc_004B268B;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B2680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B2680[BB_004B2680]
  bb_004B268B[BB_004B268B]
  bb_004B268E[BB_004B268E]
  bb_004B268F[BB_004B268F]
  bb_004B2680 -->|branch| bb_004B268F
  bb_004B2680 -->|fallthrough| bb_004B268B
  bb_004B268E -->|flow| bb_004B268F
  bb_004B268F -->|branch| bb_004B268B
```
