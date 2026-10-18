# PfSnLogIdentifier

- RVA: `0x00A7AAC8`–`0x00A7AB40` (길이 `120` bytes)
- VA: `0x0000000140A7AAC8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B6464`
- 디코드: `36`개 명령, `120/120` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A7AAEF` → [PfSnTraceGetLogEntry](../../text/34/PfSnTraceGetLogEntry_function_003437A0.md) (function, `0x003437A0`)
- `0x00A7AB09` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A7AB28` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [PfSnBeginScenario](../95/PfSnBeginScenario_function_0095EFC0.md) at `0x0095F19F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00A7AAEF` → [PfSnTraceGetLogEntry](../../text/34/PfSnTraceGetLogEntry_function_003437A0.md) (`PAGE` → `.text`)
  - `0x00A7AB09` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A7AB28` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A7AAC8  48 8B C4                        mov rax, rsp
00A7AACB  48 89 58 08                     mov qword ptr [rax + 8], rbx
00A7AACF  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00A7AAD3  57                              push rdi
00A7AAD4  48 83 EC 20                     sub rsp, 0x20
00A7AAD8  0F B7 3A                        movzx edi, word ptr [rdx]
00A7AADB  4C 8D 40 10                     lea r8, [rax + 0x10]
00A7AADF  48 83 60 10 00                  and qword ptr [rax + 0x10], 0
00A7AAE4  48 8B F2                        mov rsi, rdx
00A7AAE7  83 C7 23                        add edi, 0x23
00A7AAEA  C1 EF 04                        shr edi, 4
00A7AAED  8B D7                           mov edx, edi
00A7AAEF  E8 AC 8C 8C FF                  call 0x1403437a0
00A7AAF4  85 C0                           test eax, eax
00A7AAF6  78 37                           js 0x140a7ab2f
00A7AAF8  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
00A7AAFD  33 D2                           xor edx, edx
00A7AAFF  44 8B C7                        mov r8d, edi
00A7AB02  48 8B CB                        mov rcx, rbx
00A7AB05  49 C1 E0 04                     shl r8, 4
00A7AB09  E8 32 C1 C4 FF                  call 0x1406c6c40
00A7AB0E  8D 4F FF                        lea ecx, [rdi - 1]
00A7AB11  48 C1 E1 04                     shl rcx, 4
00A7AB15  48 83 C9 06                     or rcx, 6
00A7AB19  48 89 0B                        mov qword ptr [rbx], rcx
00A7AB1C  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00A7AB20  44 0F B7 06                     movzx r8d, word ptr [rsi]
00A7AB24  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
00A7AB28  E8 13 BD C4 FF                  call 0x1406c6840
00A7AB2D  33 C0                           xor eax, eax
00A7AB2F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A7AB34  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
00A7AB39  48 83 C4 20                     add rsp, 0x20
00A7AB3D  5F                              pop rdi
00A7AB3E  C3                              ret
00A7AB3F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfSnLogIdentifier(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (32);
    v_rdi = (unsigned int)((*(unsigned __int16 *)(a2)) + (35));
    v_rdi = (unsigned int)((v_rdi) >> (4));
    result = PfSnTraceGetLogEntry(a1, (unsigned int)((unsigned int)(v_rdi)), v_rsp + 16, a4);
    if (!(sign_flag)) {
        v_rbx = v_stack_p10;
        a2 = 0;
        a3 = (unsigned int)(v_rdi);
        a1 = v_rbx;
        a3 = (a3) << (4);
        result = memset(a1, a2, a3, a4);
        a1 = v_rdi - 1;
        a1 = (a1) << (4);
        a1 = (a1) | (6);
        *(unsigned __int64 *)(v_rbx) = a1;
        a1 = v_rbx + 16;
        a3 = *(unsigned __int16 *)(a2);
        a2 = *(unsigned __int64 *)(a2 + 8);
        result = memcpy(a1, a2, a3, a4);
        result = 0;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PfSnLogIdentifier(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (32);
    local_rdi = (uint32_t)((*(uint16_t *)(arg2)) + (35));
    local_rdi = (uint32_t)((local_rdi) >> (4));
    result = PfSnTraceGetLogEntry(Arg1, (uint32_t)((uint32_t)(local_rdi)), local_rsp + 16, a4);
    if (!(sign_flag)) {
        local_rbx = v_stack_p10;
        Arg2 = 0;
        a3 = (uint32_t)(local_rdi);
        Arg1 = local_rbx;
        a3 = (a3) << (4);
        result = memset(Arg1, Arg2, a3, a4);
        Arg1 = local_rdi - 1;
        Arg1 = (Arg1) << (4);
        Arg1 = (Arg1) | (6);
        *(uint64_t *)(local_rbx) = Arg1;
        Arg1 = local_rbx + 16;
        a3 = *(uint16_t *)(arg2);
        Arg2 = *(uint64_t *)(arg2 + 0x8);
        result = memcpy(Arg1, Arg2, a3, a4);
        result = 0;
    }
    local_rsp = (local_rsp) + (32);
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

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A7AAC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A7AAC8[BB_00A7AAC8]
  bb_00A7AAF8[BB_00A7AAF8]
  bb_00A7AB2F[BB_00A7AB2F]
  bb_00A7AB3F[BB_00A7AB3F]
  bb_00A7AAC8 -->|branch| bb_00A7AB2F
  bb_00A7AAC8 -->|fallthrough| bb_00A7AAF8
  bb_00A7AAF8 -->|flow| bb_00A7AB2F
```
