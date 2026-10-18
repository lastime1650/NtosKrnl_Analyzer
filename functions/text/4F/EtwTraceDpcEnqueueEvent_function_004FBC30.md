# EtwTraceDpcEnqueueEvent

- RVA: `0x004FBC30`–`0x004FBCCC` (길이 `156` bytes)
- VA: `0x00000001404FBC30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073CB8`
- 디코드: `40`개 명령, `156/156` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004FBCB4` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x004FBCC0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00207D3E](../20/Unknown_function_00207D3E.md) at `0x002083E1`

### Static image references
- `0x004FBC39` → RVA `0x00E0A740` (`.data`; read)
- `0x004FBC4A` → RVA `0x004A2700` (`EtwpApcPoolDpc`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FBC30  40 55                           push rbp
004FBC32  48 8B EC                        mov rbp, rsp
004FBC35  48 83 EC 70                     sub rsp, 0x70
004FBC39  48 8B 05 00 EB 90 00            mov rax, qword ptr [rip + 0x90eb00]
004FBC40  48 33 C4                        xor rax, rsp
004FBC43  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
004FBC47  45 33 D2                        xor r10d, r10d
004FBC4A  48 8D 05 AF 6A FA FF            lea rax, [rip - 0x59551]
004FBC51  66 44 89 55 D5                  mov word ptr [rbp - 0x2b], r10w
004FBC56  44 88 55 D7                     mov byte ptr [rbp - 0x29], r10b
004FBC5A  48 3B D0                        cmp rdx, rax
004FBC5D  74 5A                           je 0x1404fbcb9
004FBC5F  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
004FBC62  41 8D 52 01                     lea edx, [r10 + 1]
004FBC66  89 45 D0                        mov dword ptr [rbp - 0x30], eax
004FBC69  8A 45 38                        mov al, byte ptr [rbp + 0x38]
004FBC6C  88 45 D4                        mov byte ptr [rbp - 0x2c], al
004FBC6F  33 C0                           xor eax, eax
004FBC71  66 89 45 D5                     mov word ptr [rbp - 0x2b], ax
004FBC75  88 45 D7                        mov byte ptr [rbp - 0x29], al
004FBC78  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
004FBC7C  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
004FBC80  48 8D 45 C0                     lea rax, [rbp - 0x40]
004FBC84  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
004FBC88  48 8D 4D E0                     lea rcx, [rbp - 0x20]
004FBC8C  44 89 45 C8                     mov dword ptr [rbp - 0x38], r8d
004FBC90  41 B8 00 00 04 20               mov r8d, 0x20040000
004FBC96  44 89 4D CC                     mov dword ptr [rbp - 0x34], r9d
004FBC9A  41 B9 64 0F 00 00               mov r9d, 0xf64
004FBCA0  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
004FBCA4  48 C7 45 E8 20 00 00 00         mov qword ptr [rbp - 0x18], 0x20
004FBCAC  C7 44 24 20 02 1E 60 00         mov dword ptr [rsp + 0x20], 0x601e02
004FBCB4  E8 97 96 D3 FF                  call 0x140235350
004FBCB9  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
004FBCBD  48 33 CC                        xor rcx, rsp
004FBCC0  E8 7B 09 1B 00                  call 0x1406ac640
004FBCC5  48 83 C4 70                     add rsp, 0x70
004FBCC9  5D                              pop rbp
004FBCCA  C3                              ret
004FBCCB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceDpcEnqueueEvent(__int64 a1, __int64 a2, int a3, int a4, unsigned int a5, unsigned __int8 a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int8 v_stack_m31;
    unsigned __int16 v_stack_m33;
    unsigned __int8 v_stack_m34;
    unsigned int v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 9497344)) ^ (v_rsp);
    v_stack_m18 = result;
    v_r10 = 0;
    v_stack_m33 = 0;
    v_stack_m31 = 0;
    result = v_rip - 365905;
    if (a2 != (v_rip - 365905)) {
        result = a5;
        a2 = v_r10 + 1;
        v_stack_m38 = (unsigned int)(result);
        result = a6;
        v_stack_m34 = (unsigned __int8)(result);
        result = 0;
        v_stack_m33 = 0;
        v_stack_m31 = 0;
        result = a7;
        v_stack_m30 = result;
        result = v_stack_m48;
        v_stack_m48 = a1;
        a1 = v_stack_m28;
        v_stack_m40 = a3;
        a3 = 0x20040000ULL;
        v_stack_m3C = a4;
        a4 = 0xF64ULL;
        v_stack_m28 = result;
        v_stack_m20 = 32;
        v_stack_m58 = 0x601E02ULL;
        result = EtwTraceKernelEvent(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (112);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceDpcEnqueueEvent(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint32_t Arg5, uint8_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint8_t v_stack_m31;
    uint16_t v_stack_m33;
    uint8_t v_stack_m34;
    uint32_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x90EB00)) ^ (local_rsp);
    v_stack_m18 = result;
    local_r10 = 0;
    v_stack_m33 = 0;
    v_stack_m31 = 0;
    result = v_rip - 365905;
    if (Arg2 != (v_rip - 365905)) {
        result = Arg5;
        Arg2 = local_r10 + 1;
        v_stack_m38 = (uint32_t)(result);
        result = Arg6;
        v_stack_m34 = (uint8_t)(result);
        result = 0;
        v_stack_m33 = 0;
        v_stack_m31 = 0;
        result = Arg7;
        v_stack_m30 = result;
        result = v_stack_m48;
        v_stack_m48 = Arg1;
        Arg1 = v_stack_m28;
        v_stack_m40 = Arg3;
        Arg3 = 0x20040000ULL;
        v_stack_m3C = Arg4;
        Arg4 = 0xF64ULL;
        v_stack_m28 = result;
        v_stack_m20 = 32;
        v_stack_m58 = 0x601E02ULL;
        result = EtwTraceKernelEvent(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (112);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FBC30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FBC30[BB_004FBC30]
  bb_004FBC5F[BB_004FBC5F]
  bb_004FBCB9[BB_004FBCB9]
  bb_004FBCCB[BB_004FBCCB]
  bb_004FBC30 -->|branch| bb_004FBCB9
  bb_004FBC30 -->|fallthrough| bb_004FBC5F
  bb_004FBC5F -->|flow| bb_004FBCB9
```
