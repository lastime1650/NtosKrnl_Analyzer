# RtlpHpVsFreeChunkRemove

- RVA: `0x002E6BA0`–`0x002E6C6C` (길이 `204` bytes)
- VA: `0x00000001402E6BA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071254`
- 디코드: `59`개 명령, `204/204` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002E6BC3` → [RtlRbRemoveNode](RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)

### Direct callers
- [sub_002E6E90](Unknown_function_002E6E90.md) at `0x002E706F`

### Static image references
- `0x002E6BC8` → RVA `0x00E28302` (`.data`; read)
- `0x002E6C19` → RVA `0x00E28300` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E6BA0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002E6BA5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
002E6BAA  57                              push rdi
002E6BAB  48 83 EC 20                     sub rsp, 0x20
002E6BAF  48 8B C2                        mov rax, rdx
002E6BB2  48 8B F1                        mov rsi, rcx
002E6BB5  49 8D 51 08                     lea rdx, [r9 + 8]
002E6BB9  49 8B F9                        mov rdi, r9
002E6BBC  49 8B D8                        mov rbx, r8
002E6BBF  48 8D 48 10                     lea rcx, [rax + 0x10]
002E6BC3  E8 48 E0 FF FF                  call 0x1402e4c10
002E6BC8  0F B7 05 33 17 B4 00            movzx eax, word ptr [rip + 0xb41733]
002E6BCF  44 8B DF                        mov r11d, edi
002E6BD2  44 8B 17                        mov r10d, dword ptr [rdi]
002E6BD5  8B D7                           mov edx, edi
002E6BD7  4C 0F BF 4E 06                  movsx r9, word ptr [rsi + 6]
002E6BDC  2B D3                           sub edx, ebx
002E6BDE  81 C2 1F 10 00 00               add edx, 0x101f
002E6BE4  45 8B C2                        mov r8d, r10d
002E6BE7  44 33 C7                        xor r8d, edi
002E6BEA  41 C1 E8 10                     shr r8d, 0x10
002E6BEE  44 33 C0                        xor r8d, eax
002E6BF1  B8 00 F0 FF FF                  mov eax, 0xfffff000
002E6BF6  23 D0                           and edx, eax
002E6BF8  41 C1 E0 04                     shl r8d, 4
002E6BFC  41 8B C8                        mov ecx, r8d
002E6BFF  2B CB                           sub ecx, ebx
002E6C01  03 CF                           add ecx, edi
002E6C03  23 C8                           and ecx, eax
002E6C05  8B C1                           mov eax, ecx
002E6C07  2B C2                           sub eax, edx
002E6C09  3B D1                           cmp edx, ecx
002E6C0B  1B C9                           sbb ecx, ecx
002E6C0D  41 81 E3 FF 0F 00 00            and r11d, 0xfff
002E6C14  23 C8                           and ecx, eax
002E6C16  44 33 D7                        xor r10d, edi
002E6C19  44 33 15 E0 16 B4 00            xor r10d, dword ptr [rip + 0xb416e0]
002E6C20  C1 E9 0C                        shr ecx, 0xc
002E6C23  49 8D 83 FF 0F 00 00            lea rax, [r11 + 0xfff]
002E6C2A  41 0F B7 D2                     movzx edx, r10w
002E6C2E  49 03 C0                        add rax, r8
002E6C31  2B D1                           sub edx, ecx
002E6C33  48 C1 E8 0C                     shr rax, 0xc
002E6C37  2B D0                           sub edx, eax
002E6C39  49 8D 80 FF 0F 00 00            lea rax, [r8 + 0xfff]
002E6C40  48 C1 E8 0C                     shr rax, 0xc
002E6C44  03 D0                           add edx, eax
002E6C46  48 63 CA                        movsxd rcx, edx
002E6C49  66 45 85 C9                     test r9w, r9w
002E6C4D  74 17                           je 0x1402e6c66
002E6C4F  F0 49 01 4C 31 20               lock add qword ptr [r9 + rsi + 0x20], rcx
002E6C55  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
002E6C5A  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
002E6C5F  48 83 C4 20                     add rsp, 0x20
002E6C63  5F                              pop rdi
002E6C64  C3                              ret
002E6C65  CC                              int3
002E6C66  48 01 4E 58                     add qword ptr [rsi + 0x58], rcx
002E6C6A  EB E9                           jmp 0x1402e6c55
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpVsFreeChunkRemove(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = RtlRbRemoveNode(a2 + 16, a4 + 8, a3, a4);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) - ((unsigned int)(a3)));
    a2 = (unsigned int)((a2) + (0x101FULL));
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a4))))) ^ ((unsigned int)(a4)));
    a3 = (unsigned int)((a3) >> (16));
    a3 = (unsigned int)((a3) ^ ((unsigned int)(*(unsigned __int16 *)(v_rip + 11802419))));
    a2 = (unsigned int)((a2) & ((unsigned int)((unsigned int)(0xFFFFF000ULL))));
    a3 = (unsigned int)((a3) << (4));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(a3))) - ((unsigned int)(a3)));
    a1 = (unsigned int)((a1) + ((unsigned int)(a4)));
    a1 = (unsigned int)((a1) & ((unsigned int)((unsigned int)(0xFFFFF000ULL))));
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) - ((unsigned int)(a2)));
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(a4))) & (0xFFFULL));
    a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    v_r10 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4))) ^ ((unsigned int)(a4)));
    v_r10 = (unsigned int)((v_r10) ^ (*(unsigned int *)(v_rip + 11802336)));
    a1 = (unsigned int)((a1) >> (12));
    result = (v_r11 + 4095) + (a3);
    a2 = (unsigned int)(((unsigned __int16)(v_r10)) - ((unsigned int)(a1)));
    result = (result) >> (12);
    a2 = (unsigned int)((a2) - ((unsigned int)(result)));
    result = (a3 + 4095) >> (12);
    a2 = (unsigned int)((a2) + ((unsigned int)(result)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(a1 + 6))) == 0) goto loc_002E6C66;
loc_002E6C55:
    v_rsp = (v_rsp) + (32);
    return result;
loc_002E6C66:
    goto loc_002E6C55;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpVsFreeChunkRemove(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = RtlRbRemoveNode(Arg2 + 16, Arg4 + 8, Arg3, Arg4);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) - ((uint32_t)(Arg3)));
    Arg2 = (uint32_t)((Arg2) + (0x101FULL));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg4))))) ^ ((uint32_t)(Arg4)));
    Arg3 = (uint32_t)((Arg3) >> (16));
    Arg3 = (uint32_t)((Arg3) ^ ((uint32_t)(*(uint16_t *)(v_rip + 0xB41733))));
    Arg2 = (uint32_t)((Arg2) & ((uint32_t)((uint32_t)(0xFFFFF000ULL))));
    Arg3 = (uint32_t)((Arg3) << (4));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(Arg3))) - ((uint32_t)(Arg3)));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)(Arg4)));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)((uint32_t)(0xFFFFF000ULL))));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) - ((uint32_t)(Arg2)));
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) & (0xFFFULL));
    Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    local_r10 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4))) ^ ((uint32_t)(Arg4)));
    local_r10 = (uint32_t)((local_r10) ^ (*(uint32_t *)(v_rip + 0xB416E0)));
    Arg1 = (uint32_t)((Arg1) >> (12));
    result = (local_r11 + 4095) + (Arg3);
    Arg2 = (uint32_t)(((uint16_t)(local_r10)) - ((uint32_t)(Arg1)));
    result = (result) >> (12);
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(result)));
    result = (Arg3 + 4095) >> (12);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(result)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(arg1 + 0x6))) == 0) goto loc_002E6C66;
loc_002E6C55:
    local_rsp = (local_rsp) + (32);
    return result;
loc_002E6C66:
    goto loc_002E6C55;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x6` | `16` | `R` |
| `Arg1` | `+ 0x58` | `64` | `R/W` |
| `Arg2` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0xFFF` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E6BA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E6BA0[BB_002E6BA0]
  bb_002E6C4F[BB_002E6C4F]
  bb_002E6C55[BB_002E6C55]
  bb_002E6C65[BB_002E6C65]
  bb_002E6C66[BB_002E6C66]
  bb_002E6BA0 -->|branch| bb_002E6C66
  bb_002E6BA0 -->|fallthrough| bb_002E6C4F
  bb_002E6C4F -->|flow| bb_002E6C55
  bb_002E6C65 -->|flow| bb_002E6C66
  bb_002E6C66 -->|branch| bb_002E6C55
```
