# Feature_871661881__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F4D24`–`0x004F4D56` (길이 `50` bytes)
- VA: `0x00000001404F4D24`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F4D4B` → [Feature_871661881__private_IsEnabledFallback](Feature_871661881__private_IsEnabledFallback_function_004F4D5C.md) (function, `0x004F4D5C`)

### Direct callers
- [SepCreateAppContainerToken](SepCreateAppContainerToken_function_004F43AC.md) at `0x004F46BF`
- [NtCreateLowBoxToken](../../page/AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9EF1`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1A89`

### Static image references
- `0x004F4D2E` → RVA `0x00FC4B90` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F4D24  48 83 EC 28                     sub rsp, 0x28
004F4D28  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F4D2E  8B 05 5C FE AC 00               mov eax, dword ptr [rip + 0xacfe5c]
004F4D34  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F4D38  A8 10                           test al, 0x10
004F4D3A  74 05                           je 0x1404f4d41
004F4D3C  83 E0 01                        and eax, 1
004F4D3F  EB 0F                           jmp 0x1404f4d50
004F4D41  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F4D46  BA 03 00 00 00                  mov edx, 3
004F4D4B  E8 0C 00 00 00                  call 0x1404f4d5c
004F4D50  48 83 C4 28                     add rsp, 0x28
004F4D54  C3                              ret
004F4D55  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_871661881__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11337308)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11337308)))) & (16)) == 0) goto loc_004F4D41;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11337308))) & (1));
    goto loc_004F4D50;
loc_004F4D41:
    result = Feature_871661881__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F4D50:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_871661881__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACFE5C)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACFE5C)))) & (16)) == 0) goto loc_004F4D41;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACFE5C))) & (1));
    goto loc_004F4D50;
loc_004F4D41:
    result = Feature_871661881__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F4D50:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F4D24&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F4D24[BB_004F4D24]
  bb_004F4D3C[BB_004F4D3C]
  bb_004F4D41[BB_004F4D41]
  bb_004F4D50[BB_004F4D50]
  bb_004F4D55[BB_004F4D55]
  bb_004F4D24 -->|branch| bb_004F4D41
  bb_004F4D24 -->|fallthrough| bb_004F4D3C
  bb_004F4D3C -->|branch| bb_004F4D50
  bb_004F4D41 -->|flow| bb_004F4D50
```
