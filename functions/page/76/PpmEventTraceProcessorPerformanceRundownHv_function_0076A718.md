# PpmEventTraceProcessorPerformanceRundownHv

- RVA: `0x0076A718`–`0x0076A8FE` (길이 `486` bytes)
- VA: `0x000000014076A718`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CD248`
- 디코드: `96`개 명령, `486/486` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0076A75D` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0076A8D7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x0076A8E3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmEventTraceControlCallback](../A5/PpmEventTraceControlCallback_function_00A51F60.md) at `0x00A520A9`

### Static image references
- `0x0076A72F` → RVA `0x00E0A740` (`.data`; read)
- `0x0076A742` → RVA `0x00E67A39` (`.data`; read)
- `0x0076A74F` → RVA `0x00F083E8` (`.data`; read)
- `0x0076A756` → RVA `0x00021240` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0076A75D` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x0076A8D7` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x0076A8E3` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0076A718  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0076A71D  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
0076A722  55                              push rbp
0076A723  48 8D 6C 24 B0                  lea rbp, [rsp - 0x50]
0076A728  48 81 EC 50 01 00 00            sub rsp, 0x150
0076A72F  48 8B 05 0A 00 6A 00            mov rax, qword ptr [rip + 0x6a000a]
0076A736  48 33 C4                        xor rax, rsp
0076A739  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
0076A73D  33 FF                           xor edi, edi
0076A73F  48 8B D9                        mov rbx, rcx
0076A742  40 38 3D F0 D2 6F 00            cmp byte ptr [rip + 0x6fd2f0], dil
0076A749  0F 84 8D 01 00 00               je 0x14076a8dc
0076A74F  48 8B 0D 92 DC 79 00            mov rcx, qword ptr [rip + 0x79dc92]
0076A756  48 8D 15 E3 6A 8B FF            lea rdx, [rip - 0x74951d]
0076A75D  E8 EE 7C C2 FF                  call 0x140392450
0076A762  84 C0                           test al, al
0076A764  0F 84 72 01 00 00               je 0x14076a8dc
0076A76A  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
0076A76E  44 8D 4F 10                     lea r9d, [rdi + 0x10]
0076A772  4C 8B 03                        mov r8, qword ptr [rbx]
0076A775  48 C7 44 24 48 04 00 00 00      mov qword ptr [rsp + 0x48], 4
0076A77E  48 C7 44 24 58 04 00 00 00      mov qword ptr [rsp + 0x58], 4
0076A787  48 8D 41 14                     lea rax, [rcx + 0x14]
0076A78B  48 C7 44 24 68 04 00 00 00      mov qword ptr [rsp + 0x68], 4
0076A794  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0076A799  49 8D 90 C0 01 00 00            lea rdx, [r8 + 0x1c0]
0076A7A0  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
0076A7A4  48 8D 41 18                     lea rax, [rcx + 0x18]
0076A7A8  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0076A7AD  48 8D 41 1C                     lea rax, [rcx + 0x1c]
0076A7B1  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0076A7B6  48 8D 41 50                     lea rax, [rcx + 0x50]
0076A7BA  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0076A7BF  48 8D 41 58                     lea rax, [rcx + 0x58]
0076A7C3  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0076A7C7  48 8D 41 5C                     lea rax, [rcx + 0x5c]
0076A7CB  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0076A7CF  48 8D 41 60                     lea rax, [rcx + 0x60]
0076A7D3  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0076A7D7  48 8D 81 88 00 00 00            lea rax, [rcx + 0x88]
0076A7DE  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0076A7E2  8B C7                           mov eax, edi
0076A7E4  48 C7 44 24 78 04 00 00 00      mov qword ptr [rsp + 0x78], 4
0076A7ED  48 C7 45 88 04 00 00 00         mov qword ptr [rbp - 0x78], 4
0076A7F5  48 C7 45 98 04 00 00 00         mov qword ptr [rbp - 0x68], 4
0076A7FD  48 C7 45 A8 04 00 00 00         mov qword ptr [rbp - 0x58], 4
0076A805  48 C7 45 B8 04 00 00 00         mov qword ptr [rbp - 0x48], 4
0076A80D  48 C7 45 C8 04 00 00 00         mov qword ptr [rbp - 0x38], 4
0076A815  41 38 B8 08 02 00 00            cmp byte ptr [r8 + 0x208], dil
0076A81C  48 C7 45 D8 04 00 00 00         mov qword ptr [rbp - 0x28], 4
0076A824  0F 95 C0                        setne al
0076A827  48 C7 45 E8 04 00 00 00         mov qword ptr [rbp - 0x18], 4
0076A82F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0076A833  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0076A838  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0076A83C  48 8D 41 64                     lea rax, [rcx + 0x64]
0076A840  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0076A844  48 8D 41 68                     lea rax, [rcx + 0x68]
0076A848  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0076A84C  49 8D 80 E8 01 00 00            lea rax, [r8 + 0x1e8]
0076A853  48 89 45 00                     mov qword ptr [rbp], rax
0076A857  48 8D 41 54                     lea rax, [rcx + 0x54]
0076A85B  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
0076A85F  B8 1F 85 EB 51                  mov eax, 0x51eb851f
0076A864  48 C7 45 F8 04 00 00 00         mov qword ptr [rbp - 8], 4
0076A86C  48 C7 45 08 04 00 00 00         mov qword ptr [rbp + 8], 4
0076A874  48 C7 45 18 04 00 00 00         mov qword ptr [rbp + 0x18], 4
0076A87C  8B 89 84 00 00 00               mov ecx, dword ptr [rcx + 0x84]
0076A882  0F AF 0A                        imul ecx, dword ptr [rdx]
0076A885  48 C7 45 28 04 00 00 00         mov qword ptr [rbp + 0x28], 4
0076A88D  F7 E1                           mul ecx
0076A88F  48 8B 0D 52 DB 79 00            mov rcx, qword ptr [rip + 0x79db52]
0076A896  48 8D 44 24 34                  lea rax, [rsp + 0x34]
0076A89B  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0076A89F  C1 EA 05                        shr edx, 5
0076A8A2  89 54 24 34                     mov dword ptr [rsp + 0x34], edx
0076A8A6  48 8D 15 93 69 8B FF            lea rdx, [rip - 0x74966d]
0076A8AD  41 0F B6 80 0B 02 00 00         movzx eax, byte ptr [r8 + 0x20b]
0076A8B5  45 33 C0                        xor r8d, r8d
0076A8B8  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0076A8BC  48 8D 44 24 38                  lea rax, [rsp + 0x38]
0076A8C1  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0076A8C5  48 8D 44 24 40                  lea rax, [rsp + 0x40]
0076A8CA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0076A8CF  48 C7 45 38 04 00 00 00         mov qword ptr [rbp + 0x38], 4
0076A8D7  E8 44 1E CB FF                  call 0x14041c720
0076A8DC  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
0076A8E0  48 33 CC                        xor rcx, rsp
0076A8E3  E8 58 1D F4 FF                  call 0x1406ac640
0076A8E8  4C 8D 9C 24 50 01 00 00         lea r11, [rsp + 0x150]
0076A8F0  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0076A8F4  49 8B 7B 18                     mov rdi, qword ptr [r11 + 0x18]
0076A8F8  49 8B E3                        mov rsp, r11
0076A8FB  5D                              pop rbp
0076A8FC  C3                              ret
0076A8FD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmEventTraceProcessorPerformanceRundownHv(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (336);
    result = (*(unsigned __int64 *)(v_rip + 6946826)) ^ (v_rsp);
    v_stack_m18 = result;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 7328496)) == 0) goto loc_0076A8DC;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 7986322), v_rip - 7640349, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(a1 + 8);
        a4 = v_rdi + 16;
        a3 = *(unsigned __int64 *)(a1);
        v_stack_m110 = 4;
        v_stack_m100 = 4;
        result = a1 + 20;
        v_stack_mF0 = 4;
        v_stack_m118 = result;
        a2 = a3 + 448;
        v_stack_mD8 = a2;
        result = a1 + 24;
        v_stack_m108 = result;
        result = a1 + 28;
        v_stack_mF8 = result;
        result = a1 + 80;
        v_stack_mE8 = result;
        result = a1 + 88;
        v_stack_mC8 = result;
        result = a1 + 92;
        v_stack_mB8 = result;
        result = a1 + 96;
        v_stack_mA8 = result;
        result = a1 + 136;
        v_stack_m98 = result;
        result = 0;
        v_stack_mE0 = 4;
        v_stack_mD0 = 4;
        v_stack_mC0 = 4;
        v_stack_mB0 = 4;
        v_stack_mA0 = 4;
        v_stack_m90 = 4;
        v_stack_m80 = 4;
        result = ((*(unsigned __int8 *)(a3 + 520)) != 0) ? 1 : 0;
        v_stack_m70 = 4;
        v_stack_m128 = (unsigned int)(result);
        result = v_stack_m128;
        v_stack_m88 = result;
        result = a1 + 100;
        v_stack_m78 = result;
        result = a1 + 104;
        v_stack_m68 = result;
        result = a3 + 488;
        v_stack_m58 = result;
        result = a1 + 84;
        v_stack_m48 = result;
        result = 0x51EB851FULL;
        v_stack_m60 = 4;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        a1 = *(unsigned int *)(a1 + 132);
        a1 = (unsigned int)((a1) * (*(unsigned int *)(a2)));
        v_stack_m30 = 4;
        a1 = *(unsigned __int64 *)(v_rip + 7986002);
        result = v_stack_m124;
        v_stack_m38 = result;
        a2 = (unsigned int)((a2) >> (5));
        v_stack_m124 = (unsigned int)(a2);
        a2 = v_rip - 7640685;
        result = *(unsigned __int8 *)(a3 + 523);
        a3 = 0;
        v_stack_m120 = (unsigned int)(result);
        result = v_stack_m120;
        v_stack_m28 = result;
        result = v_stack_m118;
        v_stack_m138 = result;
        v_stack_m20 = 4;
        result = EtwWrite(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmEventTraceProcessorPerformanceRundownHv(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m124;
    uint32_t v_stack_m128;
    uint64_t v_stack_m138;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m8;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (336);
    result = (*(uint64_t *)(v_rip + 0x6A000A)) ^ (local_rsp);
    v_stack_m18 = result;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x6FD2F0)) == 0) goto loc_0076A8DC;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x79DC92), v_rip - 7640349, a3, a4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(arg1 + 0x8);
        a4 = local_rdi + 16;
        a3 = *(uint64_t *)(arg1);
        v_stack_m110 = 4;
        v_stack_m100 = 4;
        result = Arg1 + 20;
        v_stack_mF0 = 4;
        v_stack_m118 = result;
        a2 = a3 + 448;
        v_stack_mD8 = a2;
        result = Arg1 + 24;
        v_stack_m108 = result;
        result = Arg1 + 28;
        v_stack_mF8 = result;
        result = Arg1 + 80;
        v_stack_mE8 = result;
        result = Arg1 + 88;
        v_stack_mC8 = result;
        result = Arg1 + 92;
        v_stack_mB8 = result;
        result = Arg1 + 96;
        v_stack_mA8 = result;
        result = Arg1 + 136;
        v_stack_m98 = result;
        result = 0;
        v_stack_mE0 = 4;
        v_stack_mD0 = 4;
        v_stack_mC0 = 4;
        v_stack_mB0 = 4;
        v_stack_mA0 = 4;
        v_stack_m90 = 4;
        v_stack_m80 = 4;
        result = ((*(uint8_t *)(a3 + 0x208)) != 0) ? 1 : 0;
        v_stack_m70 = 4;
        v_stack_m128 = (uint32_t)(result);
        result = v_stack_m128;
        v_stack_m88 = result;
        result = Arg1 + 100;
        v_stack_m78 = result;
        result = Arg1 + 104;
        v_stack_m68 = result;
        result = a3 + 488;
        v_stack_m58 = result;
        result = Arg1 + 84;
        v_stack_m48 = result;
        result = 0x51EB851FULL;
        v_stack_m60 = 4;
        v_stack_m50 = 4;
        v_stack_m40 = 4;
        Arg1 = *(uint32_t *)(arg1 + 0x84);
        Arg1 = (uint32_t)((Arg1) * (*(uint32_t *)(a2)));
        v_stack_m30 = 4;
        Arg1 = *(uint64_t *)(v_rip + 0x79DB52);
        result = v_stack_m124;
        v_stack_m38 = result;
        a2 = (uint32_t)((a2) >> (5));
        v_stack_m124 = (uint32_t)(a2);
        a2 = v_rip - 7640685;
        result = *(uint8_t *)(a3 + 0x20B);
        a3 = 0;
        v_stack_m120 = (uint32_t)(result);
        result = v_stack_m120;
        v_stack_m28 = result;
        result = v_stack_m118;
        v_stack_m138 = result;
        v_stack_m20 = 4;
        result = EtwWrite(Arg1, a2, a3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, a2, a3, a4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0076A718&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0076A718[BB_0076A718]
  bb_0076A74F[BB_0076A74F]
  bb_0076A76A[BB_0076A76A]
  bb_0076A8DC[BB_0076A8DC]
  bb_0076A8FD[BB_0076A8FD]
  bb_0076A718 -->|branch| bb_0076A8DC
  bb_0076A718 -->|fallthrough| bb_0076A74F
  bb_0076A74F -->|branch| bb_0076A8DC
  bb_0076A74F -->|fallthrough| bb_0076A76A
  bb_0076A76A -->|flow| bb_0076A8DC
```
