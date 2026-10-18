# sub_002C2FAE

- RVA: `0x002C2FAE`–`0x002C3069` (길이 `187` bytes)
- VA: `0x00000001402C2FAE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E958`
- 디코드: `42`개 명령, `187/187` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002C2FB7` → [MiFastLockLeafPageTable](../27/MiFastLockLeafPageTable_function_00276340.md) (function, `0x00276340`)
- `0x002C304C` → [MiWalkPageTables](MiWalkPageTables_function_002C2710.md) (function, `0x002C2710`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002C3038` → RVA `0x00313710` (`MiGetNextPageTableTail`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C2FAE  45 33 C0                        xor r8d, r8d
002C2FB1  48 8B D7                        mov rdx, rdi
002C2FB4  48 8B CB                        mov rcx, rbx
002C2FB7  E8 84 33 FB FF                  call 0x140276340
002C2FBC  85 C0                           test eax, eax
002C2FBE  74 42                           je 0x1402c3002
002C2FC0  8D 50 FF                        lea edx, [rax - 1]
002C2FC3  48 C1 EF 09                     shr rdi, 9
002C2FC7  48 B8 F8 FF FF FF 7F 00 00 00   movabs rax, 0x7ffffffff8
002C2FD1  48 23 C7                        and rax, rdi
002C2FD4  49 8B CF                        mov rcx, r15
002C2FD7  48 03 C1                        add rax, rcx
002C2FDA  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
002C2FE2  89 11                           mov dword ptr [rcx], edx
002C2FE4  48 8B 9C 24 10 01 00 00         mov rbx, qword ptr [rsp + 0x110]
002C2FEC  48 8B AC 24 20 01 00 00         mov rbp, qword ptr [rsp + 0x120]
002C2FF4  48 81 C4 F0 00 00 00            add rsp, 0xf0
002C2FFB  41 5F                           pop r15
002C2FFD  41 5E                           pop r14
002C2FFF  5F                              pop rdi
002C3000  C3                              ret
002C3001  CC                              int3
002C3002  83 4C 24 30 04                  or dword ptr [rsp + 0x30], 4
002C3007  48 8D 44 24 20                  lea rax, [rsp + 0x20]
002C300C  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
002C3011  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
002C3019  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
002C301E  8B 44 24 34                     mov eax, dword ptr [rsp + 0x34]
002C3022  25 7F FE FF FF                  and eax, 0xfffffe7f
002C3027  44 88 74 24 39                  mov byte ptr [rsp + 0x39], r14b
002C302C  83 C8 40                        or eax, 0x40
002C302F  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
002C3034  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
002C3038  48 8D 05 D1 06 05 00            lea rax, [rip + 0x506d1]
002C303F  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
002C3047  48 89 6C 24 60                  mov qword ptr [rsp + 0x60], rbp
002C304C  E8 BF F6 FF FF                  call 0x1402c2710
002C3051  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
002C3055  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
002C305D  89 01                           mov dword ptr [rcx], eax
002C305F  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
002C3064  E9 7B FF FF FF                  jmp 0x1402c2fe4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002C2FAE(__int64 a1, __int64 a2, int a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p128;
    unsigned int v_stack_p13C;
    unsigned __int8 v_stack_p141;
    unsigned __int64 v_stack_p158;
    unsigned __int64 v_stack_p160;
    unsigned __int64 v_stack_p168;
    unsigned __int64 v_stack_p1E8;
    unsigned __int64 v_stack_p1F0;

    a3 = 0;
    result = MiFastLockLeafPageTable(v_rbx, v_rdi, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_002C3002;
    v_rdi = (v_rdi) >> (9);
    result = (result) & (v_rdi);
    result = (result) + (v_r15);
    *(unsigned int *)(a38) = (unsigned int)(result - 1);
loc_002C2FE4:
    v_rsp = (v_rsp) + (240);
    return result;
loc_002C3002:
    v_stack_p158 = a34;
    v_stack_p1F0 = v_stack_p128;
    result = (unsigned int)(((unsigned int)(v_stack_p13C)) & (0xFFFFFE7FULL));
    v_stack_p141 = (unsigned __int8)(v_r14);
    result = (unsigned int)((result) | (64));
    v_stack_p160 = v_rdi;
    v_stack_p13C = (unsigned int)(result);
    v_stack_p1E8 = v_rip + 329425;
    v_stack_p168 = a36;
    result = MiWalkPageTables(a6, result - 1, a3, a4);
    *(unsigned int *)(a38) = (unsigned int)((unsigned int)(v_stack_p128));
    goto loc_002C2FE4;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002C2FAE(int64_t Arg1, int64_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, int64_t Arg34, uint64_t Arg35, int64_t Arg36, uint64_t Arg37, void *Arg38)
{
    uint8_t *arg38 = (uint8_t *)Arg38;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p128;
    uint32_t v_stack_p13C;
    uint8_t v_stack_p141;
    uint64_t v_stack_p158;
    uint64_t v_stack_p160;
    uint64_t v_stack_p168;
    uint64_t v_stack_p1E8;
    uint64_t v_stack_p1F0;

    Arg3 = 0;
    result = MiFastLockLeafPageTable(local_rbx, local_rdi, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_002C3002;
    local_rdi = (local_rdi) >> (9);
    result = (result) & (local_rdi);
    result = (result) + (local_r15);
    *(uint32_t *)(arg38) = (uint32_t)(result - 1);
loc_002C2FE4:
    local_rsp = (local_rsp) + (240);
    return result;
loc_002C3002:
    v_stack_p158 = Arg34;
    v_stack_p1F0 = v_stack_p128;
    result = (uint32_t)(((uint32_t)(v_stack_p13C)) & (0xFFFFFE7FULL));
    v_stack_p141 = (uint8_t)(local_r14);
    result = (uint32_t)((result) | (64));
    v_stack_p160 = local_rdi;
    v_stack_p13C = (uint32_t)(result);
    v_stack_p1E8 = v_rip + 329425;
    v_stack_p168 = Arg36;
    result = MiWalkPageTables(Arg6, result - 1, Arg3, Arg4);
    *(uint32_t *)(arg38) = (uint32_t)((uint32_t)(v_stack_p128));
    goto loc_002C2FE4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg38` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C2FAE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C2FAE[BB_002C2FAE]
  bb_002C2FC0[BB_002C2FC0]
  bb_002C2FE4[BB_002C2FE4]
  bb_002C3001[BB_002C3001]
  bb_002C3002[BB_002C3002]
  bb_002C2FAE -->|branch| bb_002C3002
  bb_002C2FAE -->|fallthrough| bb_002C2FC0
  bb_002C2FC0 -->|flow| bb_002C2FE4
  bb_002C3001 -->|flow| bb_002C3002
  bb_002C3002 -->|branch| bb_002C2FE4
```
