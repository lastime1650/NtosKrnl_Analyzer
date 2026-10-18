# KseDsHookPoRequestPowerIrp

- RVA: `0x005CC5C0`–`0x005CC650` (길이 `144` bytes)
- VA: `0x00000001405CC5C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C7B58`
- 디코드: `40`개 명령, `144/144` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005CC603` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005CC621` → [KsepDsEventRequestPowerIrp](KsepDsEventRequestPowerIrp_function_005CD298.md) (function, `0x005CD298`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005CC5D4` → RVA `0x00E015A8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CC5C0  4C 8B DC                        mov r11, rsp
005CC5C3  49 89 5B 10                     mov qword ptr [r11 + 0x10], rbx
005CC5C7  49 89 6B 18                     mov qword ptr [r11 + 0x18], rbp
005CC5CB  49 89 73 20                     mov qword ptr [r11 + 0x20], rsi
005CC5CF  57                              push rdi
005CC5D0  48 83 EC 40                     sub rsp, 0x40
005CC5D4  48 8B 05 CD 4F 83 00            mov rax, qword ptr [rip + 0x834fcd]
005CC5DB  48 8B F1                        mov rsi, rcx
005CC5DE  49 83 63 08 00                  and qword ptr [r11 + 8], 0
005CC5E3  49 8D 4B 08                     lea rcx, [r11 + 8]
005CC5E7  41 8B D8                        mov ebx, r8d
005CC5EA  49 89 4B E0                     mov qword ptr [r11 - 0x20], rcx
005CC5EE  4C 8B 44 24 70                  mov r8, qword ptr [rsp + 0x70]
005CC5F3  48 8B CE                        mov rcx, rsi
005CC5F6  0F B6 FA                        movzx edi, dl
005CC5F9  4D 89 43 D8                     mov qword ptr [r11 - 0x28], r8
005CC5FD  40 8A D7                        mov dl, dil
005CC600  44 8B C3                        mov r8d, ebx
005CC603  E8 C8 E4 0E 00                  call 0x1406baad0
005CC608  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
005CC60D  44 8B CF                        mov r9d, edi
005CC610  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
005CC614  48 8B D6                        mov rdx, rsi
005CC617  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
005CC61B  8B E8                           mov ebp, eax
005CC61D  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
005CC621  E8 72 0C 00 00                  call 0x1405cd298
005CC626  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
005CC62B  48 85 C0                        test rax, rax
005CC62E  74 08                           je 0x1405cc638
005CC630  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
005CC635  48 89 08                        mov qword ptr [rax], rcx
005CC638  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
005CC63D  8B C5                           mov eax, ebp
005CC63F  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
005CC644  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
005CC649  48 83 C4 40                     add rsp, 0x40
005CC64D  5F                              pop rdi
005CC64E  C3                              ret
005CC64F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KseDsHookPoRequestPowerIrp(__int64 a1, unsigned __int8 a2, int a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 32) = v_rsi;
    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp + 8;
    *(unsigned __int64 *)(v_rsp - 40) = a5;
    result = guard_dispatch_icall(a1, a2, (unsigned int)((unsigned int)((unsigned int)(a3))), a4);
    v_stack_m20 = (unsigned int)(result);
    v_stack_m28 = (unsigned int)((unsigned int)(a3));
    result = KsepDsEventRequestPowerIrp(*(unsigned __int64 *)(a1 + 8), a1, v_stack_p8, (unsigned int)(a2));
    if (a6 != 0) {
        a1 = v_stack_p8;
        *(unsigned __int64 *)(a6) = a1;
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t KseDsHookPoRequestPowerIrp(void *Arg1, uint8_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rbp;
    *(uint64_t *)(local_rsp + 0x20) = local_rsi;
    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x20) = local_rsp + 8;
    *(uint64_t *)(local_rsp - 0x28) = Arg5;
    result = guard_dispatch_icall(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)(Arg3))), Arg4);
    v_stack_m20 = (uint32_t)(result);
    v_stack_m28 = (uint32_t)((uint32_t)(Arg3));
    result = KsepDsEventRequestPowerIrp(*(uint64_t *)(arg1 + 0x8), Arg1, v_stack_p8, (uint32_t)(Arg2));
    if (Arg6 != 0) {
        Arg1 = v_stack_p8;
        *(void **)(Arg6) = Arg1;
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CC5C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CC5C0[BB_005CC5C0]
  bb_005CC630[BB_005CC630]
  bb_005CC638[BB_005CC638]
  bb_005CC64F[BB_005CC64F]
  bb_005CC5C0 -->|branch| bb_005CC638
  bb_005CC5C0 -->|fallthrough| bb_005CC630
  bb_005CC630 -->|flow| bb_005CC638
```
