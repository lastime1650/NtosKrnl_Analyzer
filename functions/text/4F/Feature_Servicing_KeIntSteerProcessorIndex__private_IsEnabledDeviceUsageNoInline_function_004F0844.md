# Feature_Servicing_KeIntSteerProcessorIndex__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F0844`–`0x004F0876` (길이 `50` bytes)
- VA: `0x00000001404F0844`
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
- `0x004F086B` → [Feature_Servicing_KeIntSteerProcessorIndex__private_IsEnabledFallback](../5C/Feature_Servicing_KeIntSteerProcessorIndex__private_IsEnabledFallback_function_005C5618.md) (function, `0x005C5618`)

### Direct callers
- [KeIntSteerSnapPerf](../2D/KeIntSteerSnapPerf_function_002D76C0.md) at `0x002D7858`

### Static image references
- `0x004F084E` → RVA `0x00FC4A00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F0844  48 83 EC 28                     sub rsp, 0x28
004F0848  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F084E  8B 05 AC 41 AD 00               mov eax, dword ptr [rip + 0xad41ac]
004F0854  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F0858  A8 10                           test al, 0x10
004F085A  74 05                           je 0x1404f0861
004F085C  83 E0 01                        and eax, 1
004F085F  EB 0F                           jmp 0x1404f0870
004F0861  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F0866  BA 03 00 00 00                  mov edx, 3
004F086B  E8 A8 4D 0D 00                  call 0x1405c5618
004F0870  48 83 C4 28                     add rsp, 0x28
004F0874  C3                              ret
004F0875  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_KeIntSteerProcessorIndex__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11354540)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11354540)))) & (16)) == 0) goto loc_004F0861;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11354540))) & (1));
    goto loc_004F0870;
loc_004F0861:
    result = Feature_Servicing_KeIntSteerProcessorIndex__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F0870:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_KeIntSteerProcessorIndex__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD41AC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD41AC)))) & (16)) == 0) goto loc_004F0861;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAD41AC))) & (1));
    goto loc_004F0870;
loc_004F0861:
    result = Feature_Servicing_KeIntSteerProcessorIndex__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F0870:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F0844&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F0844[BB_004F0844]
  bb_004F085C[BB_004F085C]
  bb_004F0861[BB_004F0861]
  bb_004F0870[BB_004F0870]
  bb_004F0875[BB_004F0875]
  bb_004F0844 -->|branch| bb_004F0861
  bb_004F0844 -->|fallthrough| bb_004F085C
  bb_004F085C -->|branch| bb_004F0870
  bb_004F0861 -->|flow| bb_004F0870
```
