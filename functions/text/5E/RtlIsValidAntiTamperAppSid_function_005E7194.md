# RtlIsValidAntiTamperAppSid

- RVA: `0x005E7194`–`0x005E7206` (길이 `114` bytes)
- VA: `0x00000001405E7194`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD6E0`
- 디코드: `35`개 명령, `114/114` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005E71D1` → [RtlCompareMemory](../6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x005E71FA` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [RtlAddMandatoryAppAccessAllowedAce](../../page/78/RtlAddMandatoryAppAccessAllowedAce_function_0078D670.md) at `0x0078D6C6`

### Static image references
- `0x005E719A` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E7194  40 53                           push rbx
005E7196  48 83 EC 30                     sub rsp, 0x30
005E719A  48 8B 05 9F 35 82 00            mov rax, qword ptr [rip + 0x82359f]
005E71A1  48 33 C4                        xor rax, rsp
005E71A4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005E71A9  33 C0                           xor eax, eax
005E71AB  66 C7 44 24 24 00 14            mov word ptr [rsp + 0x24], 0x1400
005E71B2  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
005E71B6  48 8B D9                        mov rbx, rcx
005E71B9  8A 41 01                        mov al, byte ptr [rcx + 1]
005E71BC  2C 03                           sub al, 3
005E71BE  3C 05                           cmp al, 5
005E71C0  77 2E                           ja 0x1405e71f0
005E71C2  48 83 C1 02                     add rcx, 2
005E71C6  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
005E71CB  41 B8 06 00 00 00               mov r8d, 6
005E71D1  E8 9A 34 0D 00                  call 0x1406ba670
005E71D6  48 83 F8 06                     cmp rax, 6
005E71DA  75 14                           jne 0x1405e71f0
005E71DC  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
005E71DF  8D 41 FF                        lea eax, [rcx - 1]
005E71E2  83 F8 02                        cmp eax, 2
005E71E5  76 05                           jbe 0x1405e71ec
005E71E7  83 F9 05                        cmp ecx, 5
005E71EA  75 04                           jne 0x1405e71f0
005E71EC  B0 01                           mov al, 1
005E71EE  EB 02                           jmp 0x1405e71f2
005E71F0  32 C0                           xor al, al
005E71F2  48 8B 4C 24 28                  mov rcx, qword ptr [rsp + 0x28]
005E71F7  48 33 CC                        xor rcx, rsp
005E71FA  E8 41 54 0C 00                  call 0x1406ac640
005E71FF  48 83 C4 30                     add rsp, 0x30
005E7203  5B                              pop rbx
005E7204  C3                              ret
005E7205  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlIsValidAntiTamperAppSid(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int16 v_stack_m14;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (48);
    result = (*(unsigned __int64 *)(v_rip + 8533407)) ^ (v_rsp);
    v_stack_m10 = result;
    result = 0;
    v_stack_m14 = 0x1400ULL;
    v_stack_m18 = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 1)) - (3));
    if (((unsigned __int8)(result)) > 5) goto loc_005E71F0;
    a1 = (a1) + (2);
    result = RtlCompareMemory(a1, v_stack_m18, 6, a4);
    if (result != 6) goto loc_005E71F0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)) - 1)) <= 2) goto loc_005E71EC;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) != 5) goto loc_005E71F0;
loc_005E71EC:
    goto loc_005E71F2;
loc_005E71F0:
    result = 0;
loc_005E71F2:
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m18, 6, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlIsValidAntiTamperAppSid(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint16_t v_stack_m14;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    result = (*(uint64_t *)(v_rip + 0x82359F)) ^ (local_rsp);
    v_stack_m10 = result;
    result = 0;
    v_stack_m14 = 0x1400ULL;
    v_stack_m18 = 0;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x1)) - (3));
    if (((uint8_t)(result)) > 5) goto loc_005E71F0;
    Arg1 = (Arg1) + (2);
    result = RtlCompareMemory(Arg1, v_stack_m18, 6, a4);
    if (result != 6) goto loc_005E71F0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)) - 1)) <= 2) goto loc_005E71EC;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) != 5) goto loc_005E71F0;
loc_005E71EC:
    goto loc_005E71F2;
loc_005E71F0:
    result = 0;
loc_005E71F2:
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m18, 6, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1` | `8` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E7194&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E7194[BB_005E7194]
  bb_005E71C2[BB_005E71C2]
  bb_005E71DC[BB_005E71DC]
  bb_005E71E7[BB_005E71E7]
  bb_005E71EC[BB_005E71EC]
  bb_005E71F0[BB_005E71F0]
  bb_005E71F2[BB_005E71F2]
  bb_005E7205[BB_005E7205]
  bb_005E7194 -->|branch| bb_005E71F0
  bb_005E7194 -->|fallthrough| bb_005E71C2
  bb_005E71C2 -->|branch| bb_005E71F0
  bb_005E71C2 -->|fallthrough| bb_005E71DC
  bb_005E71DC -->|branch| bb_005E71EC
  bb_005E71DC -->|fallthrough| bb_005E71E7
  bb_005E71E7 -->|branch| bb_005E71F0
  bb_005E71E7 -->|fallthrough| bb_005E71EC
  bb_005E71EC -->|branch| bb_005E71F2
  bb_005E71F0 -->|flow| bb_005E71F2
```
