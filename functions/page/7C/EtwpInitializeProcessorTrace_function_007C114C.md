# EtwpInitializeProcessorTrace

- RVA: `0x007C114C`–`0x007C11B4` (길이 `104` bytes)
- VA: `0x00000001407C114C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EAB4`
- 디코드: `25`개 명령, `104/104` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x007C1198` → [ExRegisterHost](../7D/ExRegisterHost_function_007D06CC.md) (function, `0x007D06CC`)

### Direct callers
- [EtwpInitialize](../../init/C4/EtwpInitialize_function_00C4DBCC.md) at `0x00C4DD9D`

### Static image references
- `0x007C1159` → RVA `0x00009550` (`.rdata`; read)
- `0x007C1182` → RVA `0x00EFF108` (`.data`; read)
- `0x007C11A1` → RVA `0x00EFF108` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C114C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007C1151  55                              push rbp
007C1152  48 8B EC                        mov rbp, rsp
007C1155  48 83 EC 60                     sub rsp, 0x60
007C1159  48 8D 05 F0 83 84 FF            lea rax, [rip - 0x7b7c10]
007C1160  48 C7 45 D0 0B 00 01 00         mov qword ptr [rbp - 0x30], 0x1000b
007C1168  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
007C116C  4C 8D 45 D0                     lea r8, [rbp - 0x30]
007C1170  48 8D 45 C0                     lea rax, [rbp - 0x40]
007C1174  48 C7 45 E0 00 02 00 00         mov qword ptr [rbp - 0x20], 0x200
007C117C  33 DB                           xor ebx, ebx
007C117E  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
007C1182  48 8D 0D 7F DF 73 00            lea rcx, [rip + 0x73df7f]
007C1189  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
007C1190  48 89 5D E8                     mov qword ptr [rbp - 0x18], rbx
007C1194  48 89 5D F0                     mov qword ptr [rbp - 0x10], rbx
007C1198  E8 2F F5 00 00                  call 0x1407d06cc
007C119D  85 C0                           test eax, eax
007C119F  79 07                           jns 0x1407c11a8
007C11A1  48 89 1D 60 DF 73 00            mov qword ptr [rip + 0x73df60], rbx
007C11A8  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
007C11AD  48 83 C4 60                     add rsp, 0x60
007C11B1  5D                              pop rbp
007C11B2  C3                              ret
007C11B3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpInitializeProcessorTrace(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (96);
    v_stack_m38 = 0x1000BULL;
    v_stack_m40 = v_rip - 8092688;
    v_stack_m28 = 512;
    v_rbx = 0;
    v_stack_m30 = v_stack_m48;
    v_stack_m48 = 1;
    v_stack_m20 = 0;
    v_stack_m18 = 0;
    result = ExRegisterHost(v_rip + 7593855, a2, v_stack_m38, a4);
    if (sign_flag) {
        *(unsigned __int64 *)(v_rip + 7593824) = 0;
    }
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
void EtwpInitializeProcessorTrace(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (96);
    v_stack_m38 = 0x1000BULL;
    v_stack_m40 = v_rip - 8092688;
    v_stack_m28 = 512;
    local_rbx = 0;
    v_stack_m30 = v_stack_m48;
    v_stack_m48 = 1;
    v_stack_m20 = 0;
    v_stack_m18 = 0;
    result = ExRegisterHost(v_rip + 7593855, a2, v_stack_m38, a4);
    if (sign_flag) {
        *(uint64_t *)(v_rip + 0x73DF60) = 0;
    }
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C114C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007C114C[BB_007C114C]
  bb_007C11A1[BB_007C11A1]
  bb_007C11A8[BB_007C11A8]
  bb_007C11B3[BB_007C11B3]
  bb_007C114C -->|branch| bb_007C11A8
  bb_007C114C -->|fallthrough| bb_007C11A1
  bb_007C11A1 -->|flow| bb_007C11A8
```
