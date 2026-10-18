# PopDiagTraceFxPerfRequestProgress

- RVA: `0x004C1B78`–`0x004C1C52` (길이 `218` bytes)
- VA: `0x00000001404C1B78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BC83C`
- 디코드: `49`개 명령, `218/218` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x004C1BB8` → [EtwEventEnabled](../39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x004C1C2F` → [EtwWriteEx](../25/EtwWriteEx_function_0025F0D0.md) (function, `0x0025F0D0`)
- `0x004C1C3B` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_002BD95A](../2B/Unknown_function_002BD95A.md) at `0x002BDD79`
- [PopFxCompleteComponentPerfState](PopFxCompleteComponentPerfState_function_004C1750.md) at `0x004C17CD`
- [PopFxIssueComponentPerfStateChanges](PopFxIssueComponentPerfStateChanges_function_004C1940.md) at `0x004C1AC5`

### Static image references
- `0x004C1B8C` → RVA `0x00E0A740` (`.data`; read)
- `0x004C1B9A` → RVA `0x00E67858` (`.data`; read)
- `0x004C1BAA` → RVA `0x00F0B408` (`.data`; read)
- `0x004C1BB1` → RVA `0x00020E38` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004C1B78  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004C1B7D  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
004C1B81  55                              push rbp
004C1B82  48 8B EC                        mov rbp, rsp
004C1B85  48 81 EC 80 00 00 00            sub rsp, 0x80
004C1B8C  48 8B 05 AD 8B 94 00            mov rax, qword ptr [rip + 0x948bad]
004C1B93  48 33 C4                        xor rax, rsp
004C1B96  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
004C1B9A  80 3D B7 5C 9A 00 00            cmp byte ptr [rip + 0x9a5cb7], 0
004C1BA1  48 8B D9                        mov rbx, rcx
004C1BA4  0F 84 8A 00 00 00               je 0x1404c1c34
004C1BAA  48 8B 0D 57 98 A4 00            mov rcx, qword ptr [rip + 0xa49857]
004C1BB1  48 8D 15 80 F2 B5 FF            lea rdx, [rip - 0x4a0d80]
004C1BB8  E8 93 08 ED FF                  call 0x140392450
004C1BBD  84 C0                           test al, al
004C1BBF  74 73                           je 0x1404c1c34
004C1BC1  48 8B 0B                        mov rcx, qword ptr [rbx]
004C1BC4  48 8D 15 6D F2 B5 FF            lea rdx, [rip - 0x4a0d93]
004C1BCB  45 33 C9                        xor r9d, r9d
004C1BCE  45 33 C0                        xor r8d, r8d
004C1BD1  48 8B 41 50                     mov rax, qword ptr [rcx + 0x50]
004C1BD5  83 65 CC 00                     and dword ptr [rbp - 0x34], 0
004C1BD9  48 83 C0 30                     add rax, 0x30
004C1BDD  83 65 DC 00                     and dword ptr [rbp - 0x24], 0
004C1BE1  83 65 EC 00                     and dword ptr [rbp - 0x14], 0
004C1BE5  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
004C1BE9  48 8D 41 10                     lea rax, [rcx + 0x10]
004C1BED  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
004C1BF1  B9 04 00 00 00                  mov ecx, 4
004C1BF6  48 8D 45 18                     lea rax, [rbp + 0x18]
004C1BFA  89 4D D8                        mov dword ptr [rbp - 0x28], ecx
004C1BFD  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
004C1C01  48 8D 45 C0                     lea rax, [rbp - 0x40]
004C1C05  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004C1C0A  C7 44 24 30 03 00 00 00         mov dword ptr [rsp + 0x30], 3
004C1C12  48 83 64 24 28 00               and qword ptr [rsp + 0x28], 0
004C1C18  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
004C1C1E  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
004C1C21  48 8B 0D E0 97 A4 00            mov rcx, qword ptr [rip + 0xa497e0]
004C1C28  C7 45 C8 08 00 00 00            mov dword ptr [rbp - 0x38], 8
004C1C2F  E8 9C D4 D9 FF                  call 0x14025f0d0
004C1C34  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
004C1C38  48 33 CC                        xor rcx, rsp
004C1C3B  E8 00 AA 1E 00                  call 0x1406ac640
004C1C40  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
004C1C48  48 81 C4 80 00 00 00            add rsp, 0x80
004C1C4F  5D                              pop rbp
004C1C50  C3                              ret
004C1C51  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDiagTraceFxPerfRequestProgress(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (128);
    result = (*(unsigned __int64 *)(v_rip + 9735085)) ^ (v_rsp);
    v_stack_m18 = result;
    if ((*(unsigned __int8 *)(v_rip + 10116279)) == 0) goto loc_004C1C34;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 10786903), v_rip - 4853120, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a1 = *(unsigned __int64 *)(a1);
        a2 = v_rip - 4853139;
        a4 = 0;
        a3 = 0;
        result = *(unsigned __int64 *)(a1 + 80);
        result = (result) + (48);
        v_stack_m48 = result;
        result = a1 + 16;
        v_stack_m38 = result;
        a1 = 4;
        result = v_stack_p10;
        v_stack_m30 = (unsigned int)(a1);
        v_stack_m28 = result;
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m20 = (unsigned int)(a1);
        a1 = *(unsigned __int64 *)(v_rip + 10786784);
        v_stack_m40 = 8;
        result = EtwWriteEx(a1, a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDiagTraceFxPerfRequestProgress(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (128);
    result = (*(uint64_t *)(v_rip + 0x948BAD)) ^ (local_rsp);
    v_stack_m18 = result;
    if ((*(uint8_t *)(v_rip + 0x9A5CB7)) == 0) goto loc_004C1C34;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0xA49857), v_rip - 4853120, Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg1 = *(uint64_t *)(arg1);
        Arg2 = v_rip - 4853139;
        Arg4 = 0;
        Arg3 = 0;
        result = *(uint64_t *)(arg1 + 0x50);
        result = (result) + (48);
        v_stack_m48 = result;
        result = Arg1 + 16;
        v_stack_m38 = result;
        Arg1 = 4;
        result = v_stack_p10;
        v_stack_m30 = (uint32_t)(Arg1);
        v_stack_m28 = result;
        result = v_stack_m48;
        v_stack_m50 = result;
        v_stack_m58 = 3;
        v_stack_m20 = (uint32_t)(Arg1);
        Arg1 = *(uint64_t *)(v_rip + 0xA497E0);
        v_stack_m40 = 8;
        result = EtwWriteEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004C1B78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004C1B78[BB_004C1B78]
  bb_004C1BAA[BB_004C1BAA]
  bb_004C1BC1[BB_004C1BC1]
  bb_004C1C34[BB_004C1C34]
  bb_004C1C51[BB_004C1C51]
  bb_004C1B78 -->|branch| bb_004C1C34
  bb_004C1B78 -->|fallthrough| bb_004C1BAA
  bb_004C1BAA -->|branch| bb_004C1C34
  bb_004C1BAA -->|fallthrough| bb_004C1BC1
  bb_004C1BC1 -->|flow| bb_004C1C34
```
