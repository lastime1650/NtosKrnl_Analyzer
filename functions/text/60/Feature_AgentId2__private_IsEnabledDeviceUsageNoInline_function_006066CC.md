# Feature_AgentId2__private_IsEnabledDeviceUsageNoInline

- RVA: `0x006066CC`–`0x006066FE` (길이 `50` bytes)
- VA: `0x00000001406066CC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006066F3` → [Feature_AgentId2__private_IsEnabledFallback](Feature_AgentId2__private_IsEnabledFallback_function_00606704.md) (function, `0x00606704`)

### Direct callers
- [SepCreateTokenEx](../4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004EA78B`
- [SepDuplicateToken](../../page/8B/SepDuplicateToken_function_008B87EC.md) at `0x008B8B64`
- [SeTokenCanImpersonate](../../page/8C/SeTokenCanImpersonate_function_008CC4C0.md) at `0x008CC509`
- [SepFilterToken](../../page/9C/SepFilterToken_function_009C6B80.md) at `0x009C6FE1`
- [SeSubProcessToken](../../page/AA/SeSubProcessToken_function_00AAD570.md) at `0x00AADC45`
- [NtQueryInformationToken](../../page/AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEFE00`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF11DD`

### Static image references
- `0x006066D6` → RVA `0x00FC47F8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006066CC  48 83 EC 28                     sub rsp, 0x28
006066D0  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
006066D6  8B 05 1C E1 9B 00               mov eax, dword ptr [rip + 0x9be11c]
006066DC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
006066E0  A8 10                           test al, 0x10
006066E2  74 05                           je 0x1406066e9
006066E4  83 E0 01                        and eax, 1
006066E7  EB 0F                           jmp 0x1406066f8
006066E9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
006066EE  BA 03 00 00 00                  mov edx, 3
006066F3  E8 0C 00 00 00                  call 0x140606704
006066F8  48 83 C4 28                     add rsp, 0x28
006066FC  C3                              ret
006066FD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10215708)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10215708)))) & (16)) == 0) goto loc_006066E9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10215708))) & (1));
    goto loc_006066F8;
loc_006066E9:
    result = Feature_AgentId2__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_006066F8:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9BE11C)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9BE11C)))) & (16)) == 0) goto loc_006066E9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9BE11C))) & (1));
    goto loc_006066F8;
loc_006066E9:
    result = Feature_AgentId2__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_006066F8:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006066CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006066CC[BB_006066CC]
  bb_006066E4[BB_006066E4]
  bb_006066E9[BB_006066E9]
  bb_006066F8[BB_006066F8]
  bb_006066FD[BB_006066FD]
  bb_006066CC -->|branch| bb_006066E9
  bb_006066CC -->|fallthrough| bb_006066E4
  bb_006066E4 -->|branch| bb_006066F8
  bb_006066E9 -->|flow| bb_006066F8
```
