# Feature_4131803451__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0058336C`–`0x0058339E` (길이 `50` bytes)
- VA: `0x000000014058336C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00583393` → [Feature_4131803451__private_IsEnabledFallback](Feature_4131803451__private_IsEnabledFallback_function_005833A4.md) (function, `0x005833A4`)

### Direct callers
- [FsRtlCancelNotify](../4E/FsRtlCancelNotify_function_004E7F90.md) at `0x004E830B`
- [FsRtlNotifyCleanupOneEntry](../../page/A3/FsRtlNotifyCleanupOneEntry_function_00A32908.md) at `0x00A32994`
- [FsRtlNotifyFilterChangeDirectory](../../page/AA/FsRtlNotifyFilterChangeDirectory_function_00AAB9E0.md) at `0x00AABBC3`
- [FsRtlNotifyFilterChangeDirectoryLite](../../page/AD/FsRtlNotifyFilterChangeDirectoryLite_function_00ADC950.md) at `0x00ADCB04`

### Static image references
- `0x00583376` → RVA `0x00FC4740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058336C  48 83 EC 28                     sub rsp, 0x28
00583370  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00583376  8B 05 C4 13 A4 00               mov eax, dword ptr [rip + 0xa413c4]
0058337C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00583380  A8 10                           test al, 0x10
00583382  74 05                           je 0x140583389
00583384  83 E0 01                        and eax, 1
00583387  EB 0F                           jmp 0x140583398
00583389  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0058338E  BA 03 00 00 00                  mov edx, 3
00583393  E8 0C 00 00 00                  call 0x1405833a4
00583398  48 83 C4 28                     add rsp, 0x28
0058339C  C3                              ret
0058339D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_4131803451__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10752964)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10752964)))) & (16)) == 0) goto loc_00583389;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10752964))) & (1));
    goto loc_00583398;
loc_00583389:
    result = Feature_4131803451__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00583398:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_4131803451__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA413C4)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA413C4)))) & (16)) == 0) goto loc_00583389;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA413C4))) & (1));
    goto loc_00583398;
loc_00583389:
    result = Feature_4131803451__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00583398:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058336C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058336C[BB_0058336C]
  bb_00583384[BB_00583384]
  bb_00583389[BB_00583389]
  bb_00583398[BB_00583398]
  bb_0058339D[BB_0058339D]
  bb_0058336C -->|branch| bb_00583389
  bb_0058336C -->|fallthrough| bb_00583384
  bb_00583384 -->|branch| bb_00583398
  bb_00583389 -->|flow| bb_00583398
```
