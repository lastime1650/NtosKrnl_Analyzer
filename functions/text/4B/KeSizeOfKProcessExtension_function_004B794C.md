# KeSizeOfKProcessExtension

- RVA: `0x004B794C`–`0x004B797B` (길이 `47` bytes)
- VA: `0x00000001404B794C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PspAllocateProcess](../../page/A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14026`

### Static image references
- `0x004B794C` → RVA `0x00FC5014` (`ALMOSTRO`; read)
- `0x004B7964` → RVA `0x00FC6AE8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B794C  0F B7 05 C1 D6 B0 00            movzx eax, word ptr [rip + 0xb0d6c1]
004B7953  48 8D 14 40                     lea rdx, [rax + rax*2]
004B7957  48 8D 04 D5 68 02 00 00         lea rax, [rdx*8 + 0x268]
004B795F  F6 C1 04                        test cl, 4
004B7962  74 15                           je 0x1404b7979
004B7964  8B 0D 7E F1 B0 00               mov ecx, dword ptr [rip + 0xb0f17e]
004B796A  FF C9                           dec ecx
004B796C  C1 E9 03                        shr ecx, 3
004B796F  FF C1                           inc ecx
004B7971  48 8D 14 49                     lea rdx, [rcx + rcx*2]
004B7975  48 8D 04 D0                     lea rax, [rax + rdx*8]
004B7979  C3                              ret
004B797A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeSizeOfKProcessExtension(unsigned __int8 a1)
{
    __int64 result;

    result = *(unsigned __int16 *)(v_rip + 11589313) + *(unsigned __int16 *)(v_rip + 11589313) * 2 * 8 + 616;
    if (((a1) & (4)) != 0) {
        a1 = *(unsigned int *)(v_rip + 11596158);
        a1 = (unsigned int)((a1) - 1);
        a1 = (unsigned int)((a1) >> (3));
        a1 = (unsigned int)((a1) + 1);
        a2 = a1 + a1 * 2;
        result = *(unsigned __int16 *)(v_rip + 11589313) + *(unsigned __int16 *)(v_rip + 11589313) * 2 * 8 + 616 + a2 * 8;
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeSizeOfKProcessExtension(uint8_t Arg1)
{
    int64_t result;

    result = *(uint16_t *)(v_rip + 0xB0D6C1) + *(uint16_t *)(v_rip + 0xB0D6C1) * 2 * 8 + 616;
    if (((Arg1) & (4)) != 0) {
        Arg1 = *(uint32_t *)(v_rip + 0xB0F17E);
        Arg1 = (uint32_t)((Arg1) - 1);
        Arg1 = (uint32_t)((Arg1) >> (3));
        Arg1 = (uint32_t)((Arg1) + 1);
        a2 = Arg1 + Arg1 * 2;
        result = *(uint16_t *)(v_rip + 0xB0D6C1) + *(uint16_t *)(v_rip + 0xB0D6C1) * 2 * 8 + 616 + a2 * 8;
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B794C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B794C[BB_004B794C]
  bb_004B7964[BB_004B7964]
  bb_004B7979[BB_004B7979]
  bb_004B797A[BB_004B797A]
  bb_004B794C -->|branch| bb_004B7979
  bb_004B794C -->|fallthrough| bb_004B7964
  bb_004B7964 -->|flow| bb_004B7979
```
