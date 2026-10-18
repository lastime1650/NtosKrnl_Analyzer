# EtwpEventWriteTemplateSessionDesiredAccess

- RVA: `0x007B6260`–`0x007B62F2` (길이 `146` bytes)
- VA: `0x00000001407B6260`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000886E8`
- 디코드: `34`개 명령, `146/146` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x007B62D7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x007B62E3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpStartLogger](../A9/EtwpStartLogger_function_00A99D80.md) at `0x00A9A356`

### Static image references
- `0x007B626C` → RVA `0x00E0A740` (`.data`; read)
- `0x007B627E` → RVA `0x00022348` (`.rdata`; read)
- `0x007B6295` → RVA `0x000105E0` (`.rdata`; read)
- `0x007B62B7` → RVA `0x00EFF840` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007B62D7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x007B62E3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B6260  40 55                           push rbp
007B6262  48 8B EC                        mov rbp, rsp
007B6265  48 81 EC 80 00 00 00            sub rsp, 0x80
007B626C  48 8B 05 CD 44 65 00            mov rax, qword ptr [rip + 0x6544cd]
007B6273  48 33 C4                        xor rax, rsp
007B6276  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
007B627A  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
007B627E  48 8D 15 C3 C0 86 FF            lea rdx, [rip - 0x793f3d]
007B6285  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
007B6289  33 C9                           xor ecx, ecx
007B628B  41 0F B7 00                     movzx eax, word ptr [r8]
007B628F  45 33 C0                        xor r8d, r8d
007B6292  89 45 B8                        mov dword ptr [rbp - 0x48], eax
007B6295  48 8D 05 44 A3 85 FF            lea rax, [rip - 0x7a5cbc]
007B629C  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007B62A0  48 8D 45 30                     lea rax, [rbp + 0x30]
007B62A4  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
007B62A8  48 8D 45 B0                     lea rax, [rbp - 0x50]
007B62AC  4C 89 4D D0                     mov qword ptr [rbp - 0x30], r9
007B62B0  44 8D 49 04                     lea r9d, [rcx + 4]
007B62B4  89 4D BC                        mov dword ptr [rbp - 0x44], ecx
007B62B7  48 8B 0D 82 95 74 00            mov rcx, qword ptr [rip + 0x749582]
007B62BE  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007B62C3  48 C7 45 C8 02 00 00 00         mov qword ptr [rbp - 0x38], 2
007B62CB  48 C7 45 D8 10 00 00 00         mov qword ptr [rbp - 0x28], 0x10
007B62D3  4C 89 4D E8                     mov qword ptr [rbp - 0x18], r9
007B62D7  E8 44 64 C6 FF                  call 0x14041c720
007B62DC  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
007B62E0  48 33 CC                        xor rcx, rsp
007B62E3  E8 58 63 EF FF                  call 0x1406ac640
007B62E8  48 81 C4 80 00 00 00            add rsp, 0x80
007B62EF  5D                              pop rbp
007B62F0  C3                              ret
007B62F1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpEventWriteTemplateSessionDesiredAccess(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;

    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 6636749)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m58 = *(unsigned __int64 *)(a3 + 8);
    a1 = 0;
    a3 = 0;
    v_stack_m50 = (unsigned int)(*(unsigned __int16 *)(a3));
    v_stack_m48 = v_rip - 8019132;
    v_stack_m28 = a5;
    v_stack_m38 = a4;
    v_stack_m4C = 0;
    v_stack_m68 = v_stack_m58;
    v_stack_m40 = 2;
    v_stack_m30 = 16;
    v_stack_m20 = a1 + 4;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 7640450), v_rip - 7946045, a3, a1 + 4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 7946045, a3, a1 + 4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpEventWriteTemplateSessionDesiredAccess(int32_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;

    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x6544CD)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m58 = *(uint64_t *)(arg3 + 0x8);
    Arg1 = 0;
    Arg3 = 0;
    v_stack_m50 = (uint32_t)(*(uint16_t *)(arg3));
    v_stack_m48 = v_rip - 8019132;
    v_stack_m28 = Arg5;
    v_stack_m38 = Arg4;
    v_stack_m4C = 0;
    v_stack_m68 = v_stack_m58;
    v_stack_m40 = 2;
    v_stack_m30 = 16;
    v_stack_m20 = Arg1 + 4;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x749582), v_rip - 7946045, Arg3, Arg1 + 4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 7946045, Arg3, Arg1 + 4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg3` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B6260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B6260[BB_007B6260]
  bb_007B62F1[BB_007B62F1]
```
