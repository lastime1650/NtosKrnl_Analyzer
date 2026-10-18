# isprint

- RVA: `0x005006E0`–`0x00500700` (길이 `32` bytes)
- VA: `0x00000001405006E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SmSanitizeString](../60/SmSanitizeString_function_0060EC04.md) at `0x0060EC51`

### Static image references
- `0x005006EE` → RVA `0x00E00150` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005006E0  0F B6 C1                        movzx eax, cl
005006E3  83 CA FF                        or edx, 0xffffffff
005006E6  3B CA                           cmp ecx, edx
005006E8  0F 44 C2                        cmove eax, edx
005006EB  48 63 C8                        movsxd rcx, eax
005006EE  48 8B 05 5B FA 8F 00            mov rax, qword ptr [rip + 0x8ffa5b]
005006F5  0F B7 04 48                     movzx eax, word ptr [rax + rcx*2]
005006F9  25 57 01 00 00                  and eax, 0x157
005006FE  C3                              ret
005006FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall isprint(int a1, int a2)
{
    __int64 result;

    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = (unsigned __int8)(a1);
    if (a1 == a2) { result = a2; }
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9435739) + (int)((unsigned int)(result)) * 2)) & (343));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t isprint(int32_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = (uint8_t)(Arg1);
    if (Arg1 == Arg2) { result = Arg2; }
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x8FFA5B) + (int32_t)((uint32_t)(result)) * 2)) & (343));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005006E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005006E0[BB_005006E0]
  bb_005006FF[BB_005006FF]
```
