# CmFcpManagerCreateSectionFromBuffer

- RVA: `0x007F5438`–`0x007F54FB` (길이 `195` bytes)
- VA: `0x00000001407F5438`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB674`
- 디코드: `57`개 명령, `195/195` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007F5480` → [CmFcpManagerCreateSection](../AD/CmFcpManagerCreateSection_function_00ADA3BC.md) (function, `0x00ADA3BC`)
- `0x007F5493` → [CmFcpMapSection](../AC/CmFcpMapSection_function_00AC1714.md) (function, `0x00AC1714`)
- `0x007F54A8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007F54D5` → [CmFcpUnmapSection](../A4/CmFcpUnmapSection_function_00A44B8C.md) (function, `0x00A44B8C`)
- `0x007F54DE` → [CmFcpCleanupSectionState](../A3/CmFcpCleanupSectionState_function_00A304B4.md) (function, `0x00A304B4`)

### Direct callers
- [CmFcManagerOverwriteFeatureConfigurationSection](CmFcManagerOverwriteFeatureConfigurationSection_function_007F4450.md) at `0x007F46C6`
- [CmFcManagerStartRuntimePhase](../../init/C5/CmFcManagerStartRuntimePhase_function_00C5DC70.md) at `0x00C5DD7E`
- [CmFcManagerStartRuntimePhase](../../init/C5/CmFcManagerStartRuntimePhase_function_00C5DC70.md) at `0x00C5DDBC`
- [CmFcManagerStartRuntimePhase](../../init/C5/CmFcManagerStartRuntimePhase_function_00C5DC70.md) at `0x00C5DDED`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007F54A8` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007F5438  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007F543D  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
007F5442  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
007F5447  55                              push rbp
007F5448  48 8B EC                        mov rbp, rsp
007F544B  48 83 EC 50                     sub rsp, 0x50
007F544F  48 8B F1                        mov rsi, rcx
007F5452  49 8B C1                        mov rax, r9
007F5455  33 C9                           xor ecx, ecx
007F5457  4C 8D 4D D0                     lea r9, [rbp - 0x30]
007F545B  4D 8B D0                        mov r10, r8
007F545E  48 89 4D E0                     mov qword ptr [rbp - 0x20], rcx
007F5462  48 8B FA                        mov rdi, rdx
007F5465  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
007F5469  0F 57 C0                        xorps xmm0, xmm0
007F546C  0F 57 C9                        xorps xmm1, xmm1
007F546F  48 8B CF                        mov rcx, rdi
007F5472  4C 8B C0                        mov r8, rax
007F5475  49 8B D2                        mov rdx, r10
007F5478  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
007F547C  0F 11 4D E8                     movups xmmword ptr [rbp - 0x18], xmm1
007F5480  E8 37 4F 2E 00                  call 0x140ada3bc
007F5485  8B D8                           mov ebx, eax
007F5487  85 C0                           test eax, eax
007F5489  78 46                           js 0x1407f54d1
007F548B  48 8D 55 E8                     lea rdx, [rbp - 0x18]
007F548F  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007F5493  E8 7C C2 2C 00                  call 0x140ac1714
007F5498  8B D8                           mov ebx, eax
007F549A  85 C0                           test eax, eax
007F549C  78 33                           js 0x1407f54d1
007F549E  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
007F54A2  4C 8B C7                        mov r8, rdi
007F54A5  48 8B D6                        mov rdx, rsi
007F54A8  E8 93 13 ED FF                  call 0x1406c6840
007F54AD  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
007F54B1  0F 10 45 D0                     movups xmm0, xmmword ptr [rbp - 0x30]
007F54B5  F2 0F 10 4D E0                  movsd xmm1, qword ptr [rbp - 0x20]
007F54BA  0F 11 00                        movups xmmword ptr [rax], xmm0
007F54BD  F2 0F 11 48 10                  movsd qword ptr [rax + 0x10], xmm1
007F54C2  0F 57 C0                        xorps xmm0, xmm0
007F54C5  33 C0                           xor eax, eax
007F54C7  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
007F54CB  33 DB                           xor ebx, ebx
007F54CD  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
007F54D1  48 8D 4D E8                     lea rcx, [rbp - 0x18]
007F54D5  E8 B2 F6 24 00                  call 0x140a44b8c
007F54DA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007F54DE  E8 D1 AF 23 00                  call 0x140a304b4
007F54E3  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
007F54E8  8B C3                           mov eax, ebx
007F54EA  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
007F54EF  48 8B 7C 24 70                  mov rdi, qword ptr [rsp + 0x70]
007F54F4  48 83 C4 50                     add rsp, 0x50
007F54F8  5D                              pop rbp
007F54F9  C3                              ret
007F54FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmFcpManagerCreateSectionFromBuffer(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    a1 = 0;
    v_stack_m28 = 0;
    v_stack_m10 = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m20 = v_xmm1;
    result = CmFcpManagerCreateSection(a2, a3, a4, v_stack_m38);
    if (sign_flag) goto loc_007F54D1;
    result = CmFcpMapSection(v_stack_m38, v_stack_m20, a4, v_stack_m38);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a1 = v_stack_m18;
        a3 = a2;
        a2 = a1;
        result = memcpy(a1, a2, a3, v_stack_m38);
        result = a5;
        *(unsigned __int64 *)(result) = v_xmm0;
        *(unsigned __int64 *)(result + 16) = v_xmm1;
        result = 0;
        v_stack_m28 = 0;
        v_rbx = 0;
        v_stack_m38 = v_xmm0;
    }
    result = CmFcpUnmapSection(v_stack_m20, a2, a3, v_stack_m38);
    result = CmFcpCleanupSectionState(v_stack_m38, a2, a3, v_stack_m38);
    v_rsp = (v_rsp) + (80);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t CmFcpManagerCreateSectionFromBuffer(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    Arg1 = 0;
    v_stack_m28 = 0;
    v_stack_m10 = 0;
    v_stack_m38 = v_xmm0;
    v_stack_m20 = v_xmm1;
    result = CmFcpManagerCreateSection(Arg2, Arg3, Arg4, v_stack_m38);
    if (sign_flag) goto loc_007F54D1;
    result = CmFcpMapSection(v_stack_m38, v_stack_m20, Arg4, v_stack_m38);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg1 = v_stack_m18;
        Arg3 = Arg2;
        Arg2 = Arg1;
        result = memcpy(Arg1, Arg2, Arg3, v_stack_m38);
        result = Arg5;
        *(uint64_t *)(result) = v_xmm0;
        *(uint64_t *)(result + 0x10) = v_xmm1;
        result = 0;
        v_stack_m28 = 0;
        local_rbx = 0;
        v_stack_m38 = v_xmm0;
    }
    result = CmFcpUnmapSection(v_stack_m20, Arg2, Arg3, v_stack_m38);
    result = CmFcpCleanupSectionState(v_stack_m38, Arg2, Arg3, v_stack_m38);
    local_rsp = (local_rsp) + (80);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg5` | `+ 0x0` | `128` | `R` |
| `Arg5` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007F5438&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007F5438[BB_007F5438]
  bb_007F548B[BB_007F548B]
  bb_007F549E[BB_007F549E]
  bb_007F54D1[BB_007F54D1]
  bb_007F54FA[BB_007F54FA]
  bb_007F5438 -->|branch| bb_007F54D1
  bb_007F5438 -->|fallthrough| bb_007F548B
  bb_007F548B -->|branch| bb_007F54D1
  bb_007F548B -->|fallthrough| bb_007F549E
  bb_007F549E -->|flow| bb_007F54D1
```
