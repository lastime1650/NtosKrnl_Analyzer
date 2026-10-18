# KiGetInterruptObjectFromVector

- RVA: `0x0039F2B8`–`0x0039F2D7` (길이 `31` bytes)
- VA: `0x000000014039F2B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiInterruptDispatchCommon](KiInterruptDispatchCommon_function_0039F3D0.md) at `0x0039F51B`
- [KeQueryWakeSource](../5B/KeQueryWakeSource_function_005B19AC.md) at `0x005B1A3F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0039F2B8  33 C0                           xor eax, eax
0039F2BA  81 F9 FF 00 00 00               cmp ecx, 0xff
0039F2C0  77 13                           ja 0x14039f2d5
0039F2C2  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
0039F2CB  8B C1                           mov eax, ecx
0039F2CD  48 8B 84 C2 00 39 00 00         mov rax, qword ptr [rdx + rax*8 + 0x3900]
0039F2D5  C3                              ret
0039F2D6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiGetInterruptObjectFromVector(int a1)
{
    __int64 result;

    result = 0;
    if (a1 <= 255) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 32));
        result = a1;
        result = *(unsigned __int64 *)(a2 + result * 8 + 14592);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiGetInterruptObjectFromVector(int32_t Arg1)
{
    int64_t result;

    result = 0;
    if (Arg1 <= 255) {
        a2 = *(uint64_t *)(gs_base + (0 + 0x20));
        result = Arg1;
        result = *(uint64_t *)(a2 + result * 8 + 0x3900);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039F2B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0039F2B8[BB_0039F2B8]
  bb_0039F2C2[BB_0039F2C2]
  bb_0039F2D5[BB_0039F2D5]
  bb_0039F2D6[BB_0039F2D6]
  bb_0039F2B8 -->|branch| bb_0039F2D5
  bb_0039F2B8 -->|fallthrough| bb_0039F2C2
  bb_0039F2C2 -->|flow| bb_0039F2D5
```
