# EtwTraceForceParkTransition

- RVA: `0x0064F9FC`–`0x0064FA70` (길이 `116` bytes)
- VA: `0x000000014064F9FC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079788`
- 디코드: `26`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0064FA58` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x0064FA65` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [KeTraceParkingRundown](../5C/KeTraceParkingRundown_function_005C95F4.md) at `0x005C9698`
- [KiForceParkDutyCycleDpcCallback](../5C/KiForceParkDutyCycleDpcCallback_function_005C97D0.md) at `0x005C9993`

### Static image references
- `0x0064FA03` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0064F9FC  4C 8B DC                        mov r11, rsp
0064F9FF  48 83 EC 58                     sub rsp, 0x58
0064FA03  48 8B 05 36 AD 7B 00            mov rax, qword ptr [rip + 0x7bad36]
0064FA0A  48 33 C4                        xor rax, rsp
0064FA0D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0064FA12  49 83 63 D8 00                  and qword ptr [r11 - 0x28], 0
0064FA17  41 B9 7D 0F 00 00               mov r9d, 0xf7d
0064FA1D  8B 41 24                        mov eax, dword ptr [rcx + 0x24]
0064FA20  49 8D 4B E0                     lea rcx, [r11 - 0x20]
0064FA24  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0064FA28  49 8D 43 D8                     lea rax, [r11 - 0x28]
0064FA2C  88 54 24 34                     mov byte ptr [rsp + 0x34], dl
0064FA30  BA 01 00 00 00                  mov edx, 1
0064FA35  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
0064FA39  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
0064FA3E  45 88 43 DD                     mov byte ptr [r11 - 0x23], r8b
0064FA42  41 B8 00 20 00 A0               mov r8d, 0xa0002000
0064FA48  C7 44 24 40 08 00 00 00         mov dword ptr [rsp + 0x40], 8
0064FA50  C7 44 24 20 02 02 00 00         mov dword ptr [rsp + 0x20], 0x202
0064FA58  E8 F3 58 BE FF                  call 0x140235350
0064FA5D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0064FA62  48 33 CC                        xor rcx, rsp
0064FA65  E8 D6 CB 05 00                  call 0x1406ac640
0064FA6A  48 83 C4 58                     add rsp, 0x58
0064FA6E  C3                              ret
0064FA6F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceForceParkTransition(__int64 a1, unsigned __int8 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int8 v_stack_m24;
    unsigned int v_stack_m28;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 8105270)) ^ (v_rsp);
    v_stack_m10 = result;
    v_stack_m28 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36)));
    v_stack_m24 = a2;
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp - 40;
    *(unsigned __int8 *)(v_rsp - 35) = a3;
    v_stack_m18 = 8;
    v_stack_m38 = 514;
    result = EtwTraceKernelEvent(v_rsp - 32, 1, (unsigned int)(0xA0002000ULL), (unsigned int)(0xF7DULL));
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0xA0002000ULL), (unsigned int)(0xF7DULL));
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceForceParkTransition(void *Arg1, uint8_t Arg2, uint8_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint8_t v_stack_m24;
    uint32_t v_stack_m28;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x7BAD36)) ^ (local_rsp);
    v_stack_m10 = result;
    v_stack_m28 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24)));
    v_stack_m24 = Arg2;
    *(uint64_t *)(local_rsp - 0x20) = local_rsp - 40;
    *(uint8_t *)(local_rsp - 0x23) = Arg3;
    v_stack_m18 = 8;
    v_stack_m38 = 514;
    result = EtwTraceKernelEvent(local_rsp - 32, 1, (uint32_t)(0xA0002000ULL), (uint32_t)(0xF7DULL));
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0xA0002000ULL), (uint32_t)(0xF7DULL));
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x24` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0064F9FC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0064F9FC[BB_0064F9FC]
  bb_0064FA6F[BB_0064FA6F]
```
