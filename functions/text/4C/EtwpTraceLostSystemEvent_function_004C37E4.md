# EtwpTraceLostSystemEvent

- RVA: `0x004C37E4`–`0x004C38B5` (길이 `209` bytes)
- VA: `0x00000001404C37E4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCB80`
- 디코드: `47`개 명령, `209/209` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004C389A` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004C38A6` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) at `0x0025D3AF`
- [EtwpLogSystemEventUnsafe](../2F/EtwpLogSystemEventUnsafe_function_002FBF10.md) at `0x002FC656`
- [EtwpLogContextSwapEvent](../41/EtwpLogContextSwapEvent_function_004175F0.md) at `0x00417BAE`

### Static image references
- `0x004C37FB` → RVA `0x00E0A740` (`.data`; read)
- `0x004C3851` → RVA `0x000105E0` (`.rdata`; read)
- `0x004C3871` → RVA `0x00EFF840` (`.data`; read)
- `0x004C3881` → RVA `0x000105E8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C37E4  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
004C37E9  66 89 4C 24 08                  mov word ptr [rsp + 8], cx
004C37EE  55                              push rbp
004C37EF  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
004C37F4  48 81 EC 90 00 00 00            sub rsp, 0x90
004C37FB  48 8B 05 3E 6F 94 00            mov rax, qword ptr [rip + 0x946f3e]
004C3802  48 33 C4                        xor rax, rsp
004C3805  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
004C3809  45 33 D2                        xor r10d, r10d
004C380C  48 C7 45 0F 02 00 00 00         mov qword ptr [rbp + 0xf], 2
004C3814  48 8D 45 67                     lea rax, [rbp + 0x67]
004C3818  44 89 55 33                     mov dword ptr [rbp + 0x33], r10d
004C381C  48 89 45 07                     mov qword ptr [rbp + 7], rax
004C3820  45 8B C8                        mov r9d, r8d
004C3823  41 81 E1 00 02 00 00            and r9d, 0x200
004C382A  48 C7 45 3F 02 00 00 00         mov qword ptr [rbp + 0x3f], 2
004C3832  48 8D 45 7F                     lea rax, [rbp + 0x7f]
004C3836  41 0F BA E9 07                  bts r9d, 7
004C383B  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
004C383F  45 8D 5A 04                     lea r11d, [r10 + 4]
004C3843  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
004C3847  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
004C384B  0F B7 02                        movzx eax, word ptr [rdx]
004C384E  89 45 2F                        mov dword ptr [rbp + 0x2f], eax
004C3851  48 8D 05 88 CD B4 FF            lea rax, [rip - 0x4b3278]
004C3858  41 C1 E9 07                     shr r9d, 7
004C385C  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
004C3860  4C 89 5D 1F                     mov qword ptr [rbp + 0x1f], r11
004C3864  41 F7 C0 00 06 00 00            test r8d, 0x600
004C386B  74 04                           je 0x1404c3871
004C386D  41 83 C9 08                     or r9d, 8
004C3871  48 8B 0D C8 BF A3 00            mov rcx, qword ptr [rip + 0xa3bfc8]
004C3878  48 8D 45 07                     lea rax, [rbp + 7]
004C387C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004C3881  48 8D 15 60 CD B4 FF            lea rdx, [rip - 0x4b32a0]
004C3888  44 89 5C 24 30                  mov dword ptr [rsp + 0x30], r11d
004C388D  45 33 C0                        xor r8d, r8d
004C3890  4C 89 54 24 28                  mov qword ptr [rsp + 0x28], r10
004C3895  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
004C389A  E8 31 B8 D9 FF                  call 0x14025f0d0
004C389F  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
004C38A3  48 33 CC                        xor rcx, rsp
004C38A6  E8 95 8D 1E 00                  call 0x1406ac640
004C38AB  48 81 C4 90 00 00 00            add rsp, 0x90
004C38B2  5D                              pop rbp
004C38B3  C3                              ret
004C38B4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpTraceLostSystemEvent(unsigned __int16 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p20;
    unsigned __int16 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 9727806)) ^ (v_rsp);
    v_stack_m18 = result;
    v_r10 = 0;
    v_stack_m50 = 2;
    v_stack_m2C = 0;
    v_stack_m58 = v_stack_p8;
    a4 = (unsigned int)(((unsigned int)(a3)) & (512));
    v_stack_m20 = 2;
    v_stack_m48 = v_stack_p20;
    v_stack_m38 = *(unsigned __int64 *)(a2 + 8);
    v_stack_m30 = (unsigned int)(*(unsigned __int16 *)(a2));
    a4 = (unsigned int)((a4) >> (7));
    v_stack_m28 = v_rip - 4928120;
    v_stack_m40 = v_r10 + 4;
    if (((a3) & (0x600ULL)) != 0) {
        a4 = (unsigned int)((a4) | (8));
    }
    v_stack_m60 = v_stack_m58;
    v_stack_m68 = (unsigned int)(v_r10 + 4);
    a3 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    result = EtwWriteEx(*(unsigned __int64 *)(v_rip + 10731464), v_rip - 4928160, a3, a4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 4928160, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpTraceLostSystemEvent(uint16_t Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_p20;
    uint16_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x946F3E)) ^ (local_rsp);
    v_stack_m18 = result;
    local_r10 = 0;
    v_stack_m50 = 2;
    v_stack_m2C = 0;
    v_stack_m58 = v_stack_p8;
    Arg4 = (uint32_t)(((uint32_t)(Arg3)) & (512));
    v_stack_m20 = 2;
    v_stack_m48 = v_stack_p20;
    v_stack_m38 = *(uint64_t *)(arg2 + 0x8);
    v_stack_m30 = (uint32_t)(*(uint16_t *)(arg2));
    Arg4 = (uint32_t)((Arg4) >> (7));
    v_stack_m28 = v_rip - 4928120;
    v_stack_m40 = local_r10 + 4;
    if (((Arg3) & (0x600ULL)) != 0) {
        Arg4 = (uint32_t)((Arg4) | (8));
    }
    v_stack_m60 = v_stack_m58;
    v_stack_m68 = (uint32_t)(local_r10 + 4);
    Arg3 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    result = EtwWriteEx(*(uint64_t *)(v_rip + 0xA3BFC8), v_rip - 4928160, Arg3, Arg4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 4928160, Arg3, Arg4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C37E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C37E4[BB_004C37E4]
  bb_004C386D[BB_004C386D]
  bb_004C3871[BB_004C3871]
  bb_004C38B4[BB_004C38B4]
  bb_004C37E4 -->|branch| bb_004C3871
  bb_004C37E4 -->|fallthrough| bb_004C386D
  bb_004C386D -->|flow| bb_004C3871
```
