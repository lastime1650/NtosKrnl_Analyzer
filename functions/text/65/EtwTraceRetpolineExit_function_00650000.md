# EtwTraceRetpolineExit

- RVA: `0x00650000`–`0x00650064` (길이 `100` bytes)
- VA: `0x0000000140650000`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079788`
- 디코드: `22`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0065004C` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x00650059` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00650007` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00650000  4C 8B DC                        mov r11, rsp
00650003  48 83 EC 58                     sub rsp, 0x58
00650007  48 8B 05 32 A7 7B 00            mov rax, qword ptr [rip + 0x7ba732]
0065000E  48 33 C4                        xor rax, rsp
00650011  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00650016  49 8D 43 D8                     lea rax, [r11 - 0x28]
0065001A  49 89 4B D8                     mov qword ptr [r11 - 0x28], rcx
0065001E  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00650022  49 8D 4B E0                     lea rcx, [r11 - 0x20]
00650026  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
0065002B  41 B9 6E 0F 00 00               mov r9d, 0xf6e
00650031  BA 01 00 00 00                  mov edx, 1
00650036  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
0065003E  41 B8 02 00 00 A0               mov r8d, 0xa0000002
00650044  C7 44 24 20 02 0A 50 00         mov dword ptr [rsp + 0x20], 0x500a02
0065004C  E8 FF 52 BE FF                  call 0x140235350
00650051  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00650056  48 33 CC                        xor rcx, rsp
00650059  E8 E2 C5 05 00                  call 0x1406ac640
0065005E  48 83 C4 58                     add rsp, 0x58
00650062  C3                              ret
00650063  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceRetpolineExit(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 8103730)) ^ (v_rsp);
    v_stack_m10 = result;
    *(unsigned __int64 *)(v_rsp - 40) = a1;
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp - 40;
    v_stack_m18 = 8;
    v_stack_m38 = 0x500A02ULL;
    result = EtwTraceKernelEvent(v_rsp - 32, 1, (unsigned int)(0xA0000002ULL), (unsigned int)(0xF6EULL));
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0xA0000002ULL), (unsigned int)(0xF6EULL));
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceRetpolineExit(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x7BA732)) ^ (local_rsp);
    v_stack_m10 = result;
    *(uint64_t *)(local_rsp - 0x28) = Arg1;
    *(uint64_t *)(local_rsp - 0x20) = local_rsp - 40;
    v_stack_m18 = 8;
    v_stack_m38 = 0x500A02ULL;
    result = EtwTraceKernelEvent(local_rsp - 32, 1, (uint32_t)(0xA0000002ULL), (uint32_t)(0xF6EULL));
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0xA0000002ULL), (uint32_t)(0xF6EULL));
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00650000&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00650000[BB_00650000]
  bb_00650063[BB_00650063]
```
