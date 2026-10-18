# Feature_ID51912085__private_IsEnabledPreCheck

- RVA: `0x00467684`–`0x004676EC` (길이 `104` bytes)
- VA: `0x0000000140467684`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009AE6C`
- 디코드: `24`개 명령, `104/104` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004676CF` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x004676E5` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)

### Direct callers
- [PspProcessOpen](../../page/AE/PspProcessOpen_function_00AE3620.md) at `0x00AE3641`
- [NtCreateUserProcess](../../page/AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB4C3`

### Static image references
- `0x0046768E` → RVA `0x00FC4B40` (`.data`; read)
- `0x004676BF` → RVA `0x000DF0A8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00467684  48 83 EC 28                     sub rsp, 0x28
00467688  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0046768E  8B 0D AC D4 B5 00               mov ecx, dword ptr [rip + 0xb5d4ac]
00467694  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00467698  F6 C1 10                        test cl, 0x10
0046769B  74 0B                           je 0x1404676a8
0046769D  B8 01 00 00 00                  mov eax, 1
004676A2  48 83 C4 28                     add rsp, 0x28
004676A6  C3                              ret
004676A7  CC                              int3
004676A8  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
004676AD  83 C9 01                        or ecx, 1
004676B0  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004676B5  41 B9 01 00 00 00               mov r9d, 1
004676BB  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
004676BF  48 8D 0D E2 79 C7 FF            lea rcx, [rip - 0x38861e]
004676C6  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
004676CB  45 8D 41 02                     lea r8d, [r9 + 2]
004676CF  E8 10 70 0D 00                  call 0x14053e6e4
004676D4  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004676D9  4C 8D 05 C8 79 C7 FF            lea r8, [rip - 0x388638]
004676E0  BA 03 00 00 00                  mov edx, 3
004676E5  E8 8A 70 0D 00                  call 0x14053e774
004676EA  EB B1                           jmp 0x14046769d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ID51912085__private_IsEnabledPreCheck(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11916460)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11916460)))) & (16)) == 0) goto loc_004676A8;
loc_0046769D:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_004676A8:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11916460))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (unsigned int)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3704350, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3704376, 1);
    goto loc_0046769D;
}
```

## 5. (Beta) C Style

```c
void Feature_ID51912085__private_IsEnabledPreCheck(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB5D4AC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB5D4AC)))) & (16)) == 0) goto loc_004676A8;
loc_0046769D:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_004676A8:
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB5D4AC))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (uint32_t)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3704350, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3704376, 1);
    goto loc_0046769D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00467684&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00467684[BB_00467684]
  bb_0046769D[BB_0046769D]
  bb_004676A7[BB_004676A7]
  bb_004676A8[BB_004676A8]
  bb_00467684 -->|branch| bb_004676A8
  bb_00467684 -->|fallthrough| bb_0046769D
  bb_004676A7 -->|flow| bb_004676A8
  bb_004676A8 -->|branch| bb_0046769D
```
