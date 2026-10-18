# PnpQueryBusInformation

- RVA: `0x00A2AF8C`–`0x00A2B016` (길이 `138` bytes)
- VA: `0x0000000140A2AF8C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AC240`
- 디코드: `35`개 명령, `138/138` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A2AFAC` → [PpIrpQueryBusInformation](PpIrpQueryBusInformation_function_00A2B01C.md) (function, `0x00A2B01C`)
- `0x00A2AFEC` → [PnpBusTypeGuidGetIndex](PnpBusTypeGuidGetIndex_function_00A2B088.md) (function, `0x00A2B088`)
- `0x00A2B00F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiProcessNewDeviceNode](PiProcessNewDeviceNode_function_00A28F20.md) at `0x00A2A132`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A2B00F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A2AF8C  48 8B C4                        mov rax, rsp
00A2AF8F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00A2AF93  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00A2AF97  57                              push rdi
00A2AF98  48 83 EC 20                     sub rsp, 0x20
00A2AF9C  48 83 60 08 00                  and qword ptr [rax + 8], 0
00A2AFA1  48 8D 50 08                     lea rdx, [rax + 8]
00A2AFA5  48 8B F9                        mov rdi, rcx
00A2AFA8  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00A2AFAC  E8 6B 00 00 00                  call 0x140a2b01c
00A2AFB1  8B F0                           mov esi, eax
00A2AFB3  85 C0                           test eax, eax
00A2AFB5  79 2D                           jns 0x140a2afe4
00A2AFB7  66 81 8F D0 01 00 00 FF FF      or word ptr [rdi + 0x1d0], 0xffff
00A2AFC0  83 8F C8 01 00 00 FF            or dword ptr [rdi + 0x1c8], 0xffffffff
00A2AFC7  C7 87 CC 01 00 00 F0 FF FF FF   mov dword ptr [rdi + 0x1cc], 0xfffffff0
00A2AFD1  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00A2AFD6  8B C6                           mov eax, esi
00A2AFD8  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00A2AFDD  48 83 C4 20                     add rsp, 0x20
00A2AFE1  5F                              pop rdi
00A2AFE2  C3                              ret
00A2AFE3  CC                              int3
00A2AFE4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A2AFE9  48 8B CB                        mov rcx, rbx
00A2AFEC  E8 97 00 00 00                  call 0x140a2b088
00A2AFF1  66 89 87 D0 01 00 00            mov word ptr [rdi + 0x1d0], ax
00A2AFF8  48 8B CB                        mov rcx, rbx
00A2AFFB  8B 53 10                        mov edx, dword ptr [rbx + 0x10]
00A2AFFE  89 97 C8 01 00 00               mov dword ptr [rdi + 0x1c8], edx
00A2B004  8B 53 14                        mov edx, dword ptr [rbx + 0x14]
00A2B007  89 97 CC 01 00 00               mov dword ptr [rdi + 0x1cc], edx
00A2B00D  33 D2                           xor edx, edx
00A2B00F  E8 5C 78 15 00                  call 0x140b82870
00A2B014  EB BB                           jmp 0x140a2afd1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpQueryBusInformation(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p30;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = PpIrpQueryBusInformation(*(unsigned __int64 *)(a1 + 32), v_rsp + 8, a3, a4);
    if (!sign_flag) goto loc_00A2AFE4;
    *(unsigned int *)(a1 + 460) = 0xFFFFFFF0ULL;
loc_00A2AFD1:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A2AFE4:
    result = PnpBusTypeGuidGetIndex(v_stack_p30, v_rsp + 8, a3, a4);
    *(unsigned __int16 *)(a1 + 464) = (unsigned __int16)(result);
    *(unsigned int *)(a1 + 456) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p30 + 16)));
    *(unsigned int *)(a1 + 460) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p30 + 20)));
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p30, a2, a3, a4);
    goto loc_00A2AFD1;
}
```

## 5. (Beta) C Style

```c
int64_t PnpQueryBusInformation(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p30;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = PpIrpQueryBusInformation(*(uint64_t *)(arg1 + 0x20), local_rsp + 8, a3, a4);
    if (!sign_flag) goto loc_00A2AFE4;
    *(uint32_t *)(arg1 + 0x1CC) = 0xFFFFFFF0ULL;
loc_00A2AFD1:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A2AFE4:
    result = PnpBusTypeGuidGetIndex(v_stack_p30, local_rsp + 8, a3, a4);
    *(uint16_t *)(arg1 + 0x1D0) = (uint16_t)(result);
    *(uint32_t *)(arg1 + 0x1C8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p30 + 0x10)));
    *(uint32_t *)(arg1 + 0x1CC) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p30 + 0x14)));
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_p30, a2, a3, a4);
    goto loc_00A2AFD1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x1C8` | `32` | `R/W` |
| `Arg1` | `+ 0x1C8` | `32` | `W` |
| `Arg1` | `+ 0x1CC` | `32` | `W` |
| `Arg1` | `+ 0x1D0` | `16` | `R/W` |
| `Arg1` | `+ 0x1D0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A2AF8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A2AF8C[BB_00A2AF8C]
  bb_00A2AFB7[BB_00A2AFB7]
  bb_00A2AFD1[BB_00A2AFD1]
  bb_00A2AFE3[BB_00A2AFE3]
  bb_00A2AFE4[BB_00A2AFE4]
  bb_00A2AF8C -->|branch| bb_00A2AFE4
  bb_00A2AF8C -->|fallthrough| bb_00A2AFB7
  bb_00A2AFB7 -->|flow| bb_00A2AFD1
  bb_00A2AFE3 -->|flow| bb_00A2AFE4
  bb_00A2AFE4 -->|branch| bb_00A2AFD1
```
