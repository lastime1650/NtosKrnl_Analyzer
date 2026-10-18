# EtwpEventWriteProviderAccessCheckStatus

- RVA: `0x007B5D04`–`0x007B5DDF` (길이 `219` bytes)
- VA: `0x00000001407B5D04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EA9C`
- 디코드: `49`개 명령, `219/219` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x007B5DC4` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x007B5DD0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpIsRegEntryAllowed](../9E/EtwpIsRegEntryAllowed_function_009EB2D0.md) at `0x009EB44E`

### Static image references
- `0x007B5D12` → RVA `0x00E0A740` (`.data`; read)
- `0x007B5D20` → RVA `0x00EFF840` (`.data`; read)
- `0x007B5D61` → RVA `0x00014790` (`.rdata`; read)
- `0x007B5D88` → RVA `0x000105E0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x007B5DC4` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x007B5DD0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007B5D04  40 55                           push rbp
007B5D06  48 8D 6C 24 B9                  lea rbp, [rsp - 0x47]
007B5D0B  48 81 EC A0 00 00 00            sub rsp, 0xa0
007B5D12  48 8B 05 27 4A 65 00            mov rax, qword ptr [rip + 0x654a27]
007B5D19  48 33 C4                        xor rax, rsp
007B5D1C  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
007B5D20  4C 8B 15 19 9B 74 00            mov r10, qword ptr [rip + 0x749b19]
007B5D27  33 D2                           xor edx, edx
007B5D29  41 F6 41 62 02                  test byte ptr [r9 + 0x62], 2
007B5D2E  89 55 D7                        mov dword ptr [rbp - 0x29], edx
007B5D31  74 12                           je 0x1407b5d45
007B5D33  49 8B 41 50                     mov rax, qword ptr [r9 + 0x50]
007B5D37  48 85 C0                        test rax, rax
007B5D3A  74 09                           je 0x1407b5d45
007B5D3C  8B 80 D0 01 00 00               mov eax, dword ptr [rax + 0x1d0]
007B5D42  89 45 D7                        mov dword ptr [rbp - 0x29], eax
007B5D45  49 8B 41 20                     mov rax, qword ptr [r9 + 0x20]
007B5D49  45 33 C0                        xor r8d, r8d
007B5D4C  48 8B 4D 77                     mov rcx, qword ptr [rbp + 0x77]
007B5D50  48 83 C0 28                     add rax, 0x28
007B5D54  48 89 45 E7                     mov qword ptr [rbp - 0x19], rax
007B5D58  41 B9 05 00 00 00               mov r9d, 5
007B5D5E  89 55 03                        mov dword ptr [rbp + 3], edx
007B5D61  48 8D 15 28 EA 85 FF            lea rdx, [rip - 0x7a15d8]
007B5D68  48 C7 45 EF 10 00 00 00         mov qword ptr [rbp - 0x11], 0x10
007B5D70  48 8B 81 90 00 00 00            mov rax, qword ptr [rcx + 0x90]
007B5D77  48 89 45 F7                     mov qword ptr [rbp - 9], rax
007B5D7B  0F B7 81 88 00 00 00            movzx eax, word ptr [rcx + 0x88]
007B5D82  49 8B CA                        mov rcx, r10
007B5D85  89 45 FF                        mov dword ptr [rbp - 1], eax
007B5D88  48 8D 05 51 A8 85 FF            lea rax, [rip - 0x7a57af]
007B5D8F  48 89 45 07                     mov qword ptr [rbp + 7], rax
007B5D93  48 8D 45 D7                     lea rax, [rbp - 0x29]
007B5D97  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
007B5D9B  48 8D 45 7F                     lea rax, [rbp + 0x7f]
007B5D9F  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
007B5DA3  48 8D 45 E7                     lea rax, [rbp - 0x19]
007B5DA7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007B5DAC  48 C7 45 0F 02 00 00 00         mov qword ptr [rbp + 0xf], 2
007B5DB4  48 C7 45 1F 04 00 00 00         mov qword ptr [rbp + 0x1f], 4
007B5DBC  48 C7 45 2F 04 00 00 00         mov qword ptr [rbp + 0x2f], 4
007B5DC4  E8 57 69 C6 FF                  call 0x14041c720
007B5DC9  48 8B 4D 37                     mov rcx, qword ptr [rbp + 0x37]
007B5DCD  48 33 CC                        xor rcx, rsp
007B5DD0  E8 6B 68 EF FF                  call 0x1406ac640
007B5DD5  48 81 C4 A0 00 00 00            add rsp, 0xa0
007B5DDC  5D                              pop rbp
007B5DDD  C3                              ret
007B5DDE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpEventWriteProviderAccessCheckStatus(__int64 a1, int a2, int a3, __int64 a4, __int64 a5, __int64 a6)
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
    unsigned __int64 v_stack_m4F;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 6638119)) ^ (v_rsp);
    v_stack_m18 = result;
    a2 = 0;
    v_stack_m78 = 0;
    if (((*(unsigned __int8 *)(a4 + 98)) & (2)) == 0) goto loc_007B5D45;
    result = *(unsigned __int64 *)(a4 + 80);
    if (*(unsigned __int64 *)(a4 + 80) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a4 + 80) + 464);
        v_stack_m78 = (unsigned int)(result);
    }
    a3 = 0;
    result = (*(unsigned __int64 *)(a4 + 32)) + (40);
    v_stack_m68 = result;
    v_stack_m4C = 0;
    v_stack_m60 = 16;
    v_stack_m58 = *(unsigned __int64 *)(a5 + 144);
    v_stack_m50 = (unsigned int)(*(unsigned __int16 *)(a5 + 136));
    v_stack_m48 = v_rip - 8017839;
    v_stack_m38 = v_stack_m78;
    v_stack_m28 = a6;
    v_stack_m88 = v_stack_m68;
    v_stack_m40 = 2;
    v_stack_m30 = 4;
    v_stack_m20 = 4;
    result = EtwWrite(*(unsigned __int64 *)(v_rip + 7641881), v_rip - 8000984, a3, 5);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 8000984, a3, 5);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpEventWriteProviderAccessCheckStatus(int64_t Arg1, int32_t Arg2, int32_t Arg3, void *Arg4, void *Arg5, int64_t Arg6)
{
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

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
    uint64_t v_stack_m4F;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m78;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x654A27)) ^ (local_rsp);
    v_stack_m18 = result;
    Arg2 = 0;
    v_stack_m78 = 0;
    if (((*(uint8_t *)(arg4 + 0x62)) & (2)) == 0) goto loc_007B5D45;
    result = *(uint64_t *)(arg4 + 0x50);
    if (*(uint64_t *)(arg4 + 0x50) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(arg4 + 0x50) + 0x1D0);
        v_stack_m78 = (uint32_t)(result);
    }
    Arg3 = 0;
    result = (*(uint64_t *)(arg4 + 0x20)) + (40);
    v_stack_m68 = result;
    v_stack_m4C = 0;
    v_stack_m60 = 16;
    v_stack_m58 = *(uint64_t *)(arg5 + 0x90);
    v_stack_m50 = (uint32_t)(*(uint16_t *)(arg5 + 0x88));
    v_stack_m48 = v_rip - 8017839;
    v_stack_m38 = v_stack_m78;
    v_stack_m28 = Arg6;
    v_stack_m88 = v_stack_m68;
    v_stack_m40 = 2;
    v_stack_m30 = 4;
    v_stack_m20 = 4;
    result = EtwWrite(*(uint64_t *)(v_rip + 0x749B19), v_rip - 8000984, Arg3, 5);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 8000984, Arg3, 5);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x50` | `64` | `R` |
| `Arg4` | `+ 0x62` | `8` | `R` |
| `Arg5` | `+ 0x88` | `16` | `R` |
| `Arg5` | `+ 0x90` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007B5D04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007B5D04[BB_007B5D04]
  bb_007B5D33[BB_007B5D33]
  bb_007B5D3C[BB_007B5D3C]
  bb_007B5D45[BB_007B5D45]
  bb_007B5DDE[BB_007B5DDE]
  bb_007B5D04 -->|branch| bb_007B5D45
  bb_007B5D04 -->|fallthrough| bb_007B5D33
  bb_007B5D33 -->|branch| bb_007B5D45
  bb_007B5D33 -->|fallthrough| bb_007B5D3C
  bb_007B5D3C -->|flow| bb_007B5D45
```
