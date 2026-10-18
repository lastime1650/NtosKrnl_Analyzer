# HalpEfiDecrementEfiCall

- RVA: `0x00491DC0`–`0x00491DDE` (길이 `30` bytes)
- VA: `0x0000000140491DC0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [HalEfiGetTime](../54/HalEfiGetTime_function_0054DC6C.md) at `0x0054DCFE`
- [HalEfiResetSystem](../54/HalEfiResetSystem_function_0054DDE8.md) at `0x0054DE60`
- [HalEfiResetSystem](../54/HalEfiResetSystem_function_0054DDE8.md) at `0x0054DE6C`
- [HalEfiSetTime](../54/HalEfiSetTime_function_0054DE84.md) at `0x0054DF23`
- [HalEfiSetTime](../54/HalEfiSetTime_function_0054DE84.md) at `0x0054E00B`
- [HalEfiSetTime](../54/HalEfiSetTime_function_0054DE84.md) at `0x0054E017`
- [HalEfiUpdateCapsule](../54/HalEfiUpdateCapsule_function_0054E0C0.md) at `0x0054E136`
- [HalEfiUpdateCapsule](../54/HalEfiUpdateCapsule_function_0054E0C0.md) at `0x0054E142`
- [HalpQueryCapsuleCapabilities](../56/HalpQueryCapsuleCapabilities_function_00563CE0.md) at `0x00563DE2`

### Static image references
- `0x00491DC5` → RVA `0x00FC1C30` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00491DC0  83 CA FF                        or edx, 0xffffffff
00491DC3  8B C2                           mov eax, edx
00491DC5  F0 0F C1 05 63 FE B2 00         lock xadd dword ptr [rip + 0xb2fe63], eax
00491DCD  03 C2                           add eax, edx
00491DCF  48 85 C9                        test rcx, rcx
00491DD2  74 08                           je 0x140491ddc
00491DD4  8B C2                           mov eax, edx
00491DD6  F0 0F C1 01                     lock xadd dword ptr [rcx], eax
00491DDA  03 C2                           add eax, edx
00491DDC  C3                              ret
00491DDD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpEfiDecrementEfiCall(__int64 a1, int a2)
{
    __int64 result;

    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    result = (unsigned int)(((unsigned int)(a2)) + (a2));
    if (a1 != 0) {
        result = a2;
        result = (unsigned int)((result) + (a2));
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpEfiDecrementEfiCall(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    result = (uint32_t)(((uint32_t)(Arg2)) + (Arg2));
    if (Arg1 != 0) {
        result = Arg2;
        result = (uint32_t)((result) + (Arg2));
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00491DC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00491DC0[BB_00491DC0]
  bb_00491DD4[BB_00491DD4]
  bb_00491DDC[BB_00491DDC]
  bb_00491DDD[BB_00491DDD]
  bb_00491DC0 -->|branch| bb_00491DDC
  bb_00491DC0 -->|fallthrough| bb_00491DD4
  bb_00491DD4 -->|flow| bb_00491DDC
```
