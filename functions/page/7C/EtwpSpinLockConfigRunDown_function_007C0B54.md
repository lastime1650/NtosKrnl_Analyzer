# EtwpSpinLockConfigRunDown

- RVA: `0x007C0B54`–`0x007C0BE9` (길이 `149` bytes)
- VA: `0x00000001407C0B54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006F9F8`
- 디코드: `32`개 명령, `149/149` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x007C0BD1` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (function, `0x0025CC00`)
- `0x007C0BDE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpKernelTraceRundown](../9E/EtwpKernelTraceRundown_function_009E4080.md) at `0x009E41D4`

### Static image references
- `0x007C0B58` → RVA `0x00E0A740` (`.data`; read)
- `0x007C0B67` → RVA `0x00FC5150` (`ALMOSTRO`; read)
- `0x007C0B8D` → RVA `0x00FC5154` (`ALMOSTRO`; read)
- `0x007C0B97` → RVA `0x00FC5158` (`ALMOSTRO`; read)
- `0x007C0BA1` → RVA `0x00FC50D4` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007C0BD1` → [EtwpLogKernelEvent](../../text/25/EtwpLogKernelEvent_function_0025CC00.md) (`PAGE` → `.text`)
  - `0x007C0BDE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C0B54  48 83 EC 68                     sub rsp, 0x68
007C0B58  48 8B 05 E1 9B 64 00            mov rax, qword ptr [rip + 0x649be1]
007C0B5F  48 33 C4                        xor rax, rsp
007C0B62  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007C0B67  8B 05 E3 45 80 00               mov eax, dword ptr [rip + 0x8045e3]
007C0B6D  41 B9 01 00 00 00               mov r9d, 1
007C0B73  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
007C0B78  44 8B 01                        mov r8d, dword ptr [rcx]
007C0B7B  F6 DA                           neg dl
007C0B7D  48 8B 91 50 05 00 00            mov rdx, qword ptr [rcx + 0x550]
007C0B84  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
007C0B89  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
007C0B8D  8B 05 C1 45 80 00               mov eax, dword ptr [rip + 0x8045c1]
007C0B93  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
007C0B97  8B 05 BB 45 80 00               mov eax, dword ptr [rip + 0x8045bb]
007C0B9D  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
007C0BA1  8B 05 2D 45 80 00               mov eax, dword ptr [rip + 0x80452d]
007C0BA7  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
007C0BAB  48 8D 44 24 30                  lea rax, [rsp + 0x30]
007C0BB0  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007C0BB5  66 1B C0                        sbb ax, ax
007C0BB8  66 05 4C 0F                     add ax, 0xf4c
007C0BBC  C7 44 24 28 03 19 60 00         mov dword ptr [rsp + 0x28], 0x601903
007C0BC4  66 89 44 24 20                  mov word ptr [rsp + 0x20], ax
007C0BC9  C7 44 24 48 10 00 00 00         mov dword ptr [rsp + 0x48], 0x10
007C0BD1  E8 2A C0 A9 FF                  call 0x14025cc00
007C0BD6  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007C0BDB  48 33 CC                        xor rcx, rsp
007C0BDE  E8 5D BA EE FF                  call 0x1406ac640
007C0BE3  48 83 C4 68                     add rsp, 0x68
007C0BE7  C3                              ret
007C0BE8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpSpinLockConfigRunDown(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned int v_stack_m34;
    unsigned int v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int16 v_stack_m48;

    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 6593505)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = (unsigned __int8)(-(a2));
    v_stack_m38 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8406499)));
    v_stack_m30 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8406465)));
    v_stack_m34 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8406459)));
    v_stack_m2C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8406317)));
    v_stack_m28 = v_stack_m38;
    result = (unsigned __int16)((v_stack_m38) + (0xF4CULL));
    v_stack_m40 = 0x601903ULL;
    v_stack_m48 = (unsigned __int16)(result);
    v_stack_m20 = 16;
    result = EtwpLogKernelEvent(v_stack_m28, *(unsigned __int64 *)(a1 + 1360), (unsigned int)(*(unsigned int *)(a1)), 1);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(a1 + 1360), (unsigned int)(*(unsigned int *)(a1)), 1);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpSpinLockConfigRunDown(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint32_t v_stack_m34;
    uint32_t v_stack_m38;
    uint32_t v_stack_m40;
    uint16_t v_stack_m48;

    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x649BE1)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = (uint8_t)(-(Arg2));
    v_stack_m38 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8045E3)));
    v_stack_m30 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8045C1)));
    v_stack_m34 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8045BB)));
    v_stack_m2C = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x80452D)));
    v_stack_m28 = v_stack_m38;
    result = (uint16_t)((v_stack_m38) + (0xF4CULL));
    v_stack_m40 = 0x601903ULL;
    v_stack_m48 = (uint16_t)(result);
    v_stack_m20 = 16;
    result = EtwpLogKernelEvent(v_stack_m28, *(uint64_t *)(arg1 + 0x550), (uint32_t)(*(uint32_t *)(arg1)), 1);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(arg1 + 0x550), (uint32_t)(*(uint32_t *)(arg1)), 1);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x550` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C0B54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C0B54[BB_007C0B54]
  bb_007C0BE8[BB_007C0BE8]
```
