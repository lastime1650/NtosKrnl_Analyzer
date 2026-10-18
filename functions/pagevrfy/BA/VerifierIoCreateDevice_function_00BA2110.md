# VerifierIoCreateDevice

- RVA: `0x00BA2110`–`0x00BA216D` (길이 `93` bytes)
- VA: `0x0000000140BA2110`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000718C0`
- 디코드: `26`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00BA2141` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00BA215A` → [ViDevObjAdd](ViDevObjAdd_function_00BA23F4.md) (function, `0x00BA23F4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00BA2129` → RVA `0x00FFE168` (`PAGEVRFD`; read)
- `0x00BA214C` → RVA `0x00F04A20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00BA2141` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BA2110  4C 8B DC                        mov r11, rsp
00BA2113  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00BA2117  57                              push rdi
00BA2118  48 83 EC 40                     sub rsp, 0x40
00BA211C  44 8A 54 24 78                  mov r10b, byte ptr [rsp + 0x78]
00BA2121  48 8B BC 24 80 00 00 00         mov rdi, qword ptr [rsp + 0x80]
00BA2129  48 8B 05 38 C0 45 00            mov rax, qword ptr [rip + 0x45c038]
00BA2130  49 89 7B E8                     mov qword ptr [r11 - 0x18], rdi
00BA2134  45 88 53 E0                     mov byte ptr [r11 - 0x20], r10b
00BA2138  44 8B 54 24 70                  mov r10d, dword ptr [rsp + 0x70]
00BA213D  45 89 53 D8                     mov dword ptr [r11 - 0x28], r10d
00BA2141  E8 8A 89 B1 FF                  call 0x1406baad0
00BA2146  8B D8                           mov ebx, eax
00BA2148  85 C0                           test eax, eax
00BA214A  78 13                           js 0x140ba215f
00BA214C  8B 15 CE 28 36 00               mov edx, dword ptr [rip + 0x3628ce]
00BA2152  F6 C2 10                        test dl, 0x10
00BA2155  74 08                           je 0x140ba215f
00BA2157  48 8B 0F                        mov rcx, qword ptr [rdi]
00BA215A  E8 95 02 00 00                  call 0x140ba23f4
00BA215F  8B C3                           mov eax, ebx
00BA2161  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00BA2166  48 83 C4 40                     add rsp, 0x40
00BA216A  5F                              pop rdi
00BA216B  C3                              ret
00BA216C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierIoCreateDevice(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 24) = a7;
    *(unsigned __int8 *)(v_rsp - 32) = a6;
    *(unsigned int *)(v_rsp - 40) = (unsigned int)((unsigned int)(a5));
    result = guard_dispatch_icall(a1, a2, a3, a4);
    if (sign_flag) goto loc_00BA215F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 3549390)))) & (16)) != 0) {
        a1 = *(unsigned __int64 *)(a7);
        result = ViDevObjAdd(a1, (unsigned int)(*(unsigned int *)(v_rip + 3549390)), a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t VerifierIoCreateDevice(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint8_t Arg6, void *Arg7)
{
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (64);
    *(void **)(local_rsp - 0x18) = Arg7;
    *(uint8_t *)(local_rsp - 0x20) = Arg6;
    *(uint32_t *)(local_rsp - 0x28) = (uint32_t)((uint32_t)(Arg5));
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00BA215F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3628CE)))) & (16)) != 0) {
        Arg1 = *(uint64_t *)(arg7);
        result = ViDevObjAdd(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x3628CE)), Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BA2110&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BA2110[BB_00BA2110]
  bb_00BA214C[BB_00BA214C]
  bb_00BA2157[BB_00BA2157]
  bb_00BA215F[BB_00BA215F]
  bb_00BA216C[BB_00BA216C]
  bb_00BA2110 -->|branch| bb_00BA215F
  bb_00BA2110 -->|fallthrough| bb_00BA214C
  bb_00BA214C -->|branch| bb_00BA215F
  bb_00BA214C -->|fallthrough| bb_00BA2157
  bb_00BA2157 -->|flow| bb_00BA215F
```
