# CmpLogHiveInitializeEvent

- RVA: `0x007E6250`–`0x007E632F` (길이 `223` bytes)
- VA: `0x00000001407E6250`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D6C98`
- 디코드: `56`개 명령, `223/223` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007E6314` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x007E6320` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpCreateHive](../87/CmpCreateHive_function_00879DF0.md) at `0x0087A654`

### Static image references
- `0x007E626A` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007E6314` → [EtwTraceKernelEvent](../../text/23/EtwTraceKernelEvent_function_00235350.md) (`PAGE` → `.text`)
  - `0x007E6320` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E6250  48 8B C4                        mov rax, rsp
007E6253  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
007E6257  89 50 10                        mov dword ptr [rax + 0x10], edx
007E625A  48 89 48 08                     mov qword ptr [rax + 8], rcx
007E625E  55                              push rbp
007E625F  48 8D 68 A1                     lea rbp, [rax - 0x5f]
007E6263  48 81 EC B0 00 00 00            sub rsp, 0xb0
007E626A  48 8B 05 CF 44 62 00            mov rax, qword ptr [rip + 0x6244cf]
007E6271  48 33 C4                        xor rax, rsp
007E6274  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
007E6278  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
007E627C  45 33 C9                        xor r9d, r9d
007E627F  48 C7 45 EF 08 00 00 00         mov qword ptr [rbp - 0x11], 8
007E6287  8B 48 28                        mov ecx, dword ptr [rax + 0x28]
007E628A  41 8D 51 04                     lea edx, [r9 + 4]
007E628E  89 4D DB                        mov dword ptr [rbp - 0x25], ecx
007E6291  48 8D 45 67                     lea rax, [rbp + 0x67]
007E6295  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
007E6299  48 8D 45 6F                     lea rax, [rbp + 0x6f]
007E629D  48 89 45 F7                     mov qword ptr [rbp - 9], rax
007E62A1  48 8D 45 7F                     lea rax, [rbp + 0x7f]
007E62A5  48 89 45 07                     mov qword ptr [rbp + 7], rax
007E62A9  48 8D 45 DB                     lea rax, [rbp - 0x25]
007E62AD  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007E62B1  66 44 89 4D D7                  mov word ptr [rbp - 0x29], r9w
007E62B6  48 89 55 FF                     mov qword ptr [rbp - 1], rdx
007E62BA  48 89 55 0F                     mov qword ptr [rbp + 0xf], rdx
007E62BE  48 89 55 1F                     mov qword ptr [rbp + 0x1f], rdx
007E62C2  4D 85 C0                        test r8, r8
007E62C5  74 1C                           je 0x1407e62e3
007E62C7  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
007E62CB  48 85 C0                        test rax, rax
007E62CE  74 13                           je 0x1407e62e3
007E62D0  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007E62D4  41 8D 51 05                     lea edx, [r9 + 5]
007E62D8  41 0F B7 00                     movzx eax, word ptr [r8]
007E62DC  89 45 2F                        mov dword ptr [rbp + 0x2f], eax
007E62DF  44 89 4D 33                     mov dword ptr [rbp + 0x33], r9d
007E62E3  8B C2                           mov eax, edx
007E62E5  48 8D 4D D7                     lea rcx, [rbp - 0x29]
007E62E9  48 03 C0                        add rax, rax
007E62EC  C7 44 24 20 02 19 60 00         mov dword ptr [rsp + 0x20], 0x601902
007E62F4  41 B9 24 09 00 00               mov r9d, 0x924
007E62FA  FF C2                           inc edx
007E62FC  41 B8 00 00 00 41               mov r8d, 0x41000000
007E6302  48 89 4C C5 E7                  mov qword ptr [rbp + rax*8 - 0x19], rcx
007E6307  48 8D 4D E7                     lea rcx, [rbp - 0x19]
007E630B  48 C7 44 C5 EF 02 00 00 00      mov qword ptr [rbp + rax*8 - 0x11], 2
007E6314  E8 37 F0 A4 FF                  call 0x140235350
007E6319  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
007E631D  48 33 CC                        xor rcx, rsp
007E6320  E8 1B 63 EC FF                  call 0x1406ac640
007E6325  48 81 C4 B0 00 00 00            add rsp, 0xb0
007E632C  5D                              pop rbp
007E632D  C3                              ret
007E632E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLogHiveInitializeEvent(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m98;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned int *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (176);
    result = (*(unsigned __int64 *)(v_rip + 6440143)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 95 + 71) = result;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 17) = 8;
    *(unsigned int *)(v_rsp - 95 - 37) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 64) + 40)));
    *(unsigned __int64 *)(v_rsp - 95 - 25) = v_rsp - 95 + 103;
    *(unsigned __int64 *)(v_rsp - 95 - 9) = v_rsp - 95 + 111;
    *(unsigned __int64 *)(v_rsp - 95 + 7) = v_rsp - 95 + 127;
    *(unsigned __int64 *)(v_rsp - 95 + 23) = v_rsp - 95 - 37;
    *(unsigned __int16 *)(v_rsp - 95 - 41) = 0;
    *(unsigned __int64 *)(v_rsp - 95 - 1) = a4 + 4;
    *(unsigned __int64 *)(v_rsp - 95 + 15) = a4 + 4;
    *(unsigned __int64 *)(v_rsp - 95 + 31) = a4 + 4;
    if (a3 == 0) goto loc_007E62E3;
    result = *(unsigned __int64 *)(a3 + 8);
    if (*(unsigned __int64 *)(a3 + 8) != 0) {
        *(unsigned __int64 *)(v_rsp - 95 + 39) = *(unsigned __int64 *)(a3 + 8);
        a2 = a4 + 5;
        result = *(unsigned __int16 *)(a3);
        *(unsigned int *)(v_rsp - 95 + 47) = (unsigned int)(result);
        *(unsigned int *)(v_rsp - 95 + 51) = 0;
    }
    result = ((unsigned int)(a2)) + ((unsigned int)(a2));
    v_stack_m98 = 0x601902ULL;
    a2 = (unsigned int)((a2) + 1);
    *(unsigned __int64 *)(v_rsp - 95 + result * 8 - 25) = v_rsp - 95 - 41;
    *(unsigned __int64 *)(v_rsp - 95 + result * 8 - 17) = 2;
    result = EtwTraceKernelEvent(v_rsp - 95 - 25, a2, (unsigned int)(0x41000000ULL), (unsigned int)(0x924ULL));
    a1 = (*(unsigned __int64 *)(v_rsp - 95 + 71)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)(0x41000000ULL), (unsigned int)(0x924ULL));
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLogHiveInitializeEvent(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m98;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint32_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (176);
    result = (*(uint64_t *)(v_rip + 0x6244CF)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x5F + 0x47) = result;
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x11) = 8;
    *(uint32_t *)(local_rsp - 0x5F - 0x25) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x40) + 0x28)));
    *(uint64_t *)(local_rsp - 0x5F - 0x19) = local_rsp - 95 + 103;
    *(uint64_t *)(local_rsp - 0x5F - 0x9) = local_rsp - 95 + 111;
    *(uint64_t *)(local_rsp - 0x5F + 0x7) = local_rsp - 95 + 127;
    *(uint64_t *)(local_rsp - 0x5F + 0x17) = local_rsp - 95 - 37;
    *(uint16_t *)(local_rsp - 0x5F - 0x29) = 0;
    *(uint64_t *)(local_rsp - 0x5F - 0x1) = Arg4 + 4;
    *(uint64_t *)(local_rsp - 0x5F + 0xF) = Arg4 + 4;
    *(uint64_t *)(local_rsp - 0x5F + 0x1F) = Arg4 + 4;
    if (Arg3 == 0) goto loc_007E62E3;
    result = *(uint64_t *)(Arg3 + 0x8);
    if (*(uint64_t *)(Arg3 + 0x8) != 0) {
        *(uint64_t *)(local_rsp - 0x5F + 0x27) = *(uint64_t *)(Arg3 + 0x8);
        Arg2 = Arg4 + 5;
        result = *(uint16_t *)(Arg3);
        *(uint32_t *)(local_rsp - 0x5F + 0x2F) = (uint32_t)(result);
        *(uint32_t *)(local_rsp - 0x5F + 0x33) = 0;
    }
    result = ((uint32_t)(Arg2)) + ((uint32_t)(Arg2));
    v_stack_m98 = 0x601902ULL;
    Arg2 = (uint32_t)((Arg2) + 1);
    *(uint64_t *)(local_rsp - 0x5F + result * 8 - 0x19) = local_rsp - 95 - 41;
    *(uint64_t *)(local_rsp - 0x5F + result * 8 - 0x11) = 2;
    result = EtwTraceKernelEvent(local_rsp - 95 - 25, Arg2, (uint32_t)(0x41000000ULL), (uint32_t)(0x924ULL));
    Arg1 = (*(uint64_t *)(local_rsp - 0x5F + 0x47)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)(0x41000000ULL), (uint32_t)(0x924ULL));
    local_rsp = (local_rsp) + (176);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E6250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E6250[BB_007E6250]
  bb_007E62C7[BB_007E62C7]
  bb_007E62D0[BB_007E62D0]
  bb_007E62E3[BB_007E62E3]
  bb_007E632E[BB_007E632E]
  bb_007E6250 -->|branch| bb_007E62E3
  bb_007E6250 -->|fallthrough| bb_007E62C7
  bb_007E62C7 -->|branch| bb_007E62E3
  bb_007E62C7 -->|fallthrough| bb_007E62D0
  bb_007E62D0 -->|flow| bb_007E62E3
```
