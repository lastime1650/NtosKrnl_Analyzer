# Feature_IldeLatencyAwareStandbyStealing__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F7A40`–`0x004F7A72` (길이 `50` bytes)
- VA: `0x00000001404F7A40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F7A67` → [Feature_IldeLatencyAwareStandbyStealing__private_IsEnabledFallback](Feature_IldeLatencyAwareStandbyStealing__private_IsEnabledFallback_function_004F7A78.md) (function, `0x004F7A78`)

### Direct callers
- [KiInitializeVelocity](../../init/BE/KiInitializeVelocity_function_00BEEDB8.md) at `0x00BEEE05`

### Static image references
- `0x004F7A4A` → RVA `0x00FC48F8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F7A40  48 83 EC 28                     sub rsp, 0x28
004F7A44  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F7A4A  8B 05 A8 CE AC 00               mov eax, dword ptr [rip + 0xaccea8]
004F7A50  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F7A54  A8 10                           test al, 0x10
004F7A56  74 05                           je 0x1404f7a5d
004F7A58  83 E0 01                        and eax, 1
004F7A5B  EB 0F                           jmp 0x1404f7a6c
004F7A5D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F7A62  BA 03 00 00 00                  mov edx, 3
004F7A67  E8 0C 00 00 00                  call 0x1404f7a78
004F7A6C  48 83 C4 28                     add rsp, 0x28
004F7A70  C3                              ret
004F7A71  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_IldeLatencyAwareStandbyStealing__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11325096)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11325096)))) & (16)) == 0) goto loc_004F7A5D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11325096))) & (1));
    goto loc_004F7A6C;
loc_004F7A5D:
    result = Feature_IldeLatencyAwareStandbyStealing__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7A6C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_IldeLatencyAwareStandbyStealing__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACCEA8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACCEA8)))) & (16)) == 0) goto loc_004F7A5D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACCEA8))) & (1));
    goto loc_004F7A6C;
loc_004F7A5D:
    result = Feature_IldeLatencyAwareStandbyStealing__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F7A6C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F7A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F7A40[BB_004F7A40]
  bb_004F7A58[BB_004F7A58]
  bb_004F7A5D[BB_004F7A5D]
  bb_004F7A6C[BB_004F7A6C]
  bb_004F7A71[BB_004F7A71]
  bb_004F7A40 -->|branch| bb_004F7A5D
  bb_004F7A40 -->|fallthrough| bb_004F7A58
  bb_004F7A58 -->|branch| bb_004F7A6C
  bb_004F7A5D -->|flow| bb_004F7A6C
```
