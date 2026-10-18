# Feature_Servicing_CompressSecureHiberdata__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0058DE10`–`0x0058DE42` (길이 `50` bytes)
- VA: `0x000000014058DE10`
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
- `0x0058DE37` → [Feature_Servicing_CompressSecureHiberdata__private_IsEnabledFallback](Feature_Servicing_CompressSecureHiberdata__private_IsEnabledFallback_function_0058DE48.md) (function, `0x0058DE48`)

### Direct callers
- [VslAllocateSecureHibernateResources](../../page/71/VslAllocateSecureHibernateResources_function_00718788.md) at `0x007187C3`

### Static image references
- `0x0058DE1A` → RVA `0x00FC4758` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058DE10  48 83 EC 28                     sub rsp, 0x28
0058DE14  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0058DE1A  8B 05 38 69 A3 00               mov eax, dword ptr [rip + 0xa36938]
0058DE20  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0058DE24  A8 10                           test al, 0x10
0058DE26  74 05                           je 0x14058de2d
0058DE28  83 E0 01                        and eax, 1
0058DE2B  EB 0F                           jmp 0x14058de3c
0058DE2D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0058DE32  BA 03 00 00 00                  mov edx, 3
0058DE37  E8 0C 00 00 00                  call 0x14058de48
0058DE3C  48 83 C4 28                     add rsp, 0x28
0058DE40  C3                              ret
0058DE41  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_CompressSecureHiberdata__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10709304)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10709304)))) & (16)) == 0) goto loc_0058DE2D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10709304))) & (1));
    goto loc_0058DE3C;
loc_0058DE2D:
    result = Feature_Servicing_CompressSecureHiberdata__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0058DE3C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_CompressSecureHiberdata__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA36938)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA36938)))) & (16)) == 0) goto loc_0058DE2D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA36938))) & (1));
    goto loc_0058DE3C;
loc_0058DE2D:
    result = Feature_Servicing_CompressSecureHiberdata__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0058DE3C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058DE10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058DE10[BB_0058DE10]
  bb_0058DE28[BB_0058DE28]
  bb_0058DE2D[BB_0058DE2D]
  bb_0058DE3C[BB_0058DE3C]
  bb_0058DE41[BB_0058DE41]
  bb_0058DE10 -->|branch| bb_0058DE2D
  bb_0058DE10 -->|fallthrough| bb_0058DE28
  bb_0058DE28 -->|branch| bb_0058DE3C
  bb_0058DE2D -->|flow| bb_0058DE3C
```
