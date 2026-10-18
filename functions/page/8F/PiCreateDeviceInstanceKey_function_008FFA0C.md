# PiCreateDeviceInstanceKey

- RVA: `0x008FFA0C`–`0x008FFAB4` (길이 `168` bytes)
- VA: `0x00000001408FFA0C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000883D4`
- 디코드: `43`개 명령, `168/168` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x008FFA4B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008FFA73` → [CmCreateDevice](CmCreateDevice_function_008FFABC.md) (function, `0x008FFABC`)
- `0x008FFA85` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008FFA8A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PiProcessNewDeviceNode](../A2/PiProcessNewDeviceNode_function_00A28F20.md) at `0x00A292BC`

### Static image references
- `0x008FFA32` → RVA `0x00F8C600` (`.data`; read)
- `0x008FFA61` → RVA `0x00E66398` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008FFA4B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008FFA85` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008FFA8A` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008FFA0C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
008FFA11  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
008FFA16  57                              push rdi
008FFA17  48 83 EC 30                     sub rsp, 0x30
008FFA1B  48 83 22 00                     and qword ptr [rdx], 0
008FFA1F  48 8B DA                        mov rbx, rdx
008FFA22  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008FFA2B  48 8B F9                        mov rdi, rcx
008FFA2E  41 83 20 00                     and dword ptr [r8], 0
008FFA32  48 8D 0D C7 CB 68 00            lea rcx, [rip + 0x68cbc7]
008FFA39  B2 01                           mov dl, 1
008FFA3B  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
008FFA40  49 8B F0                        mov rsi, r8
008FFA43  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008FFA4A  90                              nop
008FFA4B  E8 70 21 91 FF                  call 0x140211bc0
008FFA50  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
008FFA55  48 8D 44 24 40                  lea rax, [rsp + 0x40]
008FFA5A  48 8B 57 30                     mov rdx, qword ptr [rdi + 0x30]
008FFA5E  4C 8B CB                        mov r9, rbx
008FFA61  48 8B 0D 30 69 56 00            mov rcx, qword ptr [rip + 0x566930]
008FFA68  41 B8 3F 00 0F 00               mov r8d, 0xf003f
008FFA6E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008FFA73  E8 44 00 00 00                  call 0x1408ffabc
008FFA78  8B D8                           mov ebx, eax
008FFA7A  85 C0                           test eax, eax
008FFA7C  79 24                           jns 0x1408ffaa2
008FFA7E  48 8D 0D 7B CB 68 00            lea rcx, [rip + 0x68cb7b]
008FFA85  E8 86 FF 95 FF                  call 0x14025fa10
008FFA8A  E8 21 DE 95 FF                  call 0x14025d8b0
008FFA8F  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
008FFA94  8B C3                           mov eax, ebx
008FFA96  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008FFA9B  48 83 C4 30                     add rsp, 0x30
008FFA9F  5F                              pop rdi
008FFAA0  C3                              ret
008FFAA1  CC                              int3
008FFAA2  8A 54 24 40                     mov dl, byte ptr [rsp + 0x40]
008FFAA6  F6 DA                           neg dl
008FFAA8  45 1B C0                        sbb r8d, r8d
008FFAAB  41 83 C0 02                     add r8d, 2
008FFAAF  44 89 06                        mov dword ptr [rsi], r8d
008FFAB2  EB CA                           jmp 0x1408ffa7e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCreateDeviceInstanceKey(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p40;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (48);
    v_stack_p8 = 0;
    result = ExAcquireResourceSharedLite(v_rip + 6867911, 1, a3, a4);
    v_stack_m18 = v_stack_p8;
    result = CmCreateDevice(*(unsigned __int64 *)(v_rip + 5663024), *(unsigned __int64 *)(a1 + 48), (unsigned int)(0xF003FULL), a2);
    if (!sign_flag) goto loc_008FFAA2;
loc_008FFA7E:
    result = ExReleaseResourceLite(v_rip + 6867835, *(unsigned __int64 *)(a1 + 48), (unsigned int)(0xF003FULL), a2);
    result = KeLeaveCriticalRegion(v_rip + 6867835, *(unsigned __int64 *)(a1 + 48), (unsigned int)(0xF003FULL), a2);
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008FFAA2:
    a2 = (unsigned __int8)(-(v_stack_p40));
    a3 = (unsigned int)(((unsigned int)(0xF003FULL)) + (2));
    *(unsigned int *)(v_stack_p18) = (unsigned int)(a3);
    goto loc_008FFA7E;
}
```

## 5. (Beta) C Style

```c
int64_t PiCreateDeviceInstanceKey(void *Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p40;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (48);
    v_stack_p8 = 0;
    result = ExAcquireResourceSharedLite(v_rip + 6867911, 1, Arg3, a4);
    v_stack_m18 = v_stack_p8;
    result = CmCreateDevice(*(uint64_t *)(v_rip + 0x566930), *(uint64_t *)(arg1 + 0x30), (uint32_t)(0xF003FULL), Arg2);
    if (!sign_flag) goto loc_008FFAA2;
loc_008FFA7E:
    result = ExReleaseResourceLite(v_rip + 6867835, *(uint64_t *)(arg1 + 0x30), (uint32_t)(0xF003FULL), Arg2);
    result = KeLeaveCriticalRegion(v_rip + 6867835, *(uint64_t *)(arg1 + 0x30), (uint32_t)(0xF003FULL), Arg2);
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008FFAA2:
    Arg2 = (uint8_t)(-(v_stack_p40));
    Arg3 = (uint32_t)(((uint32_t)(0xF003FULL)) + (2));
    *(uint32_t *)(v_stack_p18) = (uint32_t)(Arg3);
    goto loc_008FFA7E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg3` | `+ 0x0` | `32` | `R/W` |
| `Arg3` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FFA0C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008FFA0C[BB_008FFA0C]
  bb_008FFA7E[BB_008FFA7E]
  bb_008FFAA1[BB_008FFAA1]
  bb_008FFAA2[BB_008FFAA2]
  bb_008FFA0C -->|branch| bb_008FFAA2
  bb_008FFA0C -->|fallthrough| bb_008FFA7E
  bb_008FFAA1 -->|flow| bb_008FFAA2
  bb_008FFAA2 -->|branch| bb_008FFA7E
```
