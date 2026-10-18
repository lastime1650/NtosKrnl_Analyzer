# Feature_CvmDmaBouncing__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0054C96C`–`0x0054C99E` (길이 `50` bytes)
- VA: `0x000000014054C96C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0054C993` → [Feature_CvmDmaBouncing__private_IsEnabledFallback](Feature_CvmDmaBouncing__private_IsEnabledFallback_function_0054C9A4.md) (function, `0x0054C9A4`)

### Direct callers
- [HalpEnlightenmentInitialize](HalpEnlightenmentInitialize_function_0054C9C0.md) at `0x0054CDC4`
- [HalpDmaInit](../../init/C2/HalpDmaInit_function_00C20D34.md) at `0x00C20D46`

### Static image references
- `0x0054C976` → RVA `0x00FC4658` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054C96C  48 83 EC 28                     sub rsp, 0x28
0054C970  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0054C976  8B 05 DC 7C A7 00               mov eax, dword ptr [rip + 0xa77cdc]
0054C97C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0054C980  A8 10                           test al, 0x10
0054C982  74 05                           je 0x14054c989
0054C984  83 E0 01                        and eax, 1
0054C987  EB 0F                           jmp 0x14054c998
0054C989  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054C98E  BA 03 00 00 00                  mov edx, 3
0054C993  E8 0C 00 00 00                  call 0x14054c9a4
0054C998  48 83 C4 28                     add rsp, 0x28
0054C99C  C3                              ret
0054C99D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_CvmDmaBouncing__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10976476)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10976476)))) & (16)) == 0) goto loc_0054C989;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10976476))) & (1));
    goto loc_0054C998;
loc_0054C989:
    result = Feature_CvmDmaBouncing__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0054C998:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_CvmDmaBouncing__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA77CDC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA77CDC)))) & (16)) == 0) goto loc_0054C989;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA77CDC))) & (1));
    goto loc_0054C998;
loc_0054C989:
    result = Feature_CvmDmaBouncing__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0054C998:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054C96C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054C96C[BB_0054C96C]
  bb_0054C984[BB_0054C984]
  bb_0054C989[BB_0054C989]
  bb_0054C998[BB_0054C998]
  bb_0054C99D[BB_0054C99D]
  bb_0054C96C -->|branch| bb_0054C989
  bb_0054C96C -->|fallthrough| bb_0054C984
  bb_0054C984 -->|branch| bb_0054C998
  bb_0054C989 -->|flow| bb_0054C998
```
