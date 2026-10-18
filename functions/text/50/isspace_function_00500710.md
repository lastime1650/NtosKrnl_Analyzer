# isspace

- RVA: `0x00500710`–`0x0050072E` (길이 `30` bytes)
- VA: `0x0000000140500710`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [ScTrimString](../6A/ScTrimString_function_006A4120.md) at `0x006A4160`
- [ScTrimString](../6A/ScTrimString_function_006A4120.md) at `0x006A4190`
- [CmpGetToken](../../init/C2/CmpGetToken_function_00C28488.md) at `0x00C284C9`
- [CmpGetToken](../../init/C2/CmpGetToken_function_00C28488.md) at `0x00C28557`

### Static image references
- `0x0050071E` → RVA `0x00E00150` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00500710  0F B6 C1                        movzx eax, cl
00500713  83 CA FF                        or edx, 0xffffffff
00500716  3B CA                           cmp ecx, edx
00500718  0F 44 C2                        cmove eax, edx
0050071B  48 63 C8                        movsxd rcx, eax
0050071E  48 8B 05 2B FA 8F 00            mov rax, qword ptr [rip + 0x8ffa2b]
00500725  0F B7 04 48                     movzx eax, word ptr [rax + rcx*2]
00500729  83 E0 08                        and eax, 8
0050072C  C3                              ret
0050072D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall isspace(int a1, int a2)
{
    __int64 result;

    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = (unsigned __int8)(a1);
    if (a1 == a2) { result = a2; }
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 9435691) + (int)((unsigned int)(result)) * 2)) & (8));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t isspace(int32_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = (uint8_t)(Arg1);
    if (Arg1 == Arg2) { result = Arg2; }
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x8FFA2B) + (int32_t)((uint32_t)(result)) * 2)) & (8));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00500710&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00500710[BB_00500710]
  bb_0050072D[BB_0050072D]
```
