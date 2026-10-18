# CmpLogClearAccessBitsEvent

- RVA: `0x0087C64C`–`0x0087C6F9` (길이 `173` bytes)
- VA: `0x000000014087C64C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF6C`
- 디코드: `43`개 명령, `173/173` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0087C6DE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (function, `0x0041C720`)
- `0x0087C6EA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpClearKeyAccessBits](CmpClearKeyAccessBits_function_0087BB5C.md) at `0x0087BCAE`

### Static image references
- `0x0087C662` → RVA `0x00E0A740` (`.data`; read)
- `0x0087C676` → RVA `0x00EFFA28` (`.data`; read)
- `0x0087C693` → RVA `0x00020DC0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0087C6DE` → [EtwWrite](../../text/41/EtwWrite_function_0041C720.md) (`PAGE` → `.text`)
  - `0x0087C6EA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0087C64C  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0087C651  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0087C655  55                              push rbp
0087C656  48 8D 6C 24 A9                  lea rbp, [rsp - 0x57]
0087C65B  48 81 EC 90 00 00 00            sub rsp, 0x90
0087C662  48 8B 05 D7 E0 58 00            mov rax, qword ptr [rip + 0x58e0d7]
0087C669  48 33 C4                        xor rax, rsp
0087C66C  48 89 45 47                     mov qword ptr [rbp + 0x47], rax
0087C670  4C 8B C1                        mov r8, rcx
0087C673  45 33 D2                        xor r10d, r10d
0087C676  48 8B 0D AB 33 68 00            mov rcx, qword ptr [rip + 0x6833ab]
0087C67D  48 85 C9                        test rcx, rcx
0087C680  74 61                           je 0x14087c6e3
0087C682  41 0F B7 10                     movzx edx, word ptr [r8]
0087C686  45 8D 4A 04                     lea r9d, [r10 + 4]
0087C68A  0F B7 C2                        movzx eax, dx
0087C68D  89 55 1F                        mov dword ptr [rbp + 0x1f], edx
0087C690  66 D1 E8                        shr ax, 1
0087C693  48 8D 15 26 47 7A FF            lea rdx, [rip - 0x85b8da]
0087C69A  66 89 45 F7                     mov word ptr [rbp - 9], ax
0087C69E  48 8D 45 F7                     lea rax, [rbp - 9]
0087C6A2  48 89 45 07                     mov qword ptr [rbp + 7], rax
0087C6A6  49 8B 40 08                     mov rax, qword ptr [r8 + 8]
0087C6AA  45 33 C0                        xor r8d, r8d
0087C6AD  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
0087C6B1  48 8D 45 6F                     lea rax, [rbp + 0x6f]
0087C6B5  48 89 45 27                     mov qword ptr [rbp + 0x27], rax
0087C6B9  48 8D 45 77                     lea rax, [rbp + 0x77]
0087C6BD  48 89 45 37                     mov qword ptr [rbp + 0x37], rax
0087C6C1  48 8D 45 07                     lea rax, [rbp + 7]
0087C6C5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0087C6CA  48 C7 45 0F 02 00 00 00         mov qword ptr [rbp + 0xf], 2
0087C6D2  44 89 55 23                     mov dword ptr [rbp + 0x23], r10d
0087C6D6  4C 89 4D 2F                     mov qword ptr [rbp + 0x2f], r9
0087C6DA  4C 89 4D 3F                     mov qword ptr [rbp + 0x3f], r9
0087C6DE  E8 3D 00 BA FF                  call 0x14041c720
0087C6E3  48 8B 4D 47                     mov rcx, qword ptr [rbp + 0x47]
0087C6E7  48 33 CC                        xor rcx, rsp
0087C6EA  E8 51 FF E2 FF                  call 0x1406ac640
0087C6EF  48 81 C4 90 00 00 00            add rsp, 0x90
0087C6F6  5D                              pop rbp
0087C6F7  C3                              ret
0087C6F8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLogClearAccessBitsEvent(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m3C;
    unsigned int v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int16 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 5824727)) ^ (v_rsp);
    v_stack_m18 = result;
    v_r10 = 0;
    if (*(unsigned __int64 *)(v_rip + 6828971) != 0) {
        a2 = *(unsigned __int16 *)(a1);
        a4 = v_r10 + 4;
        result = (unsigned __int16)(a2);
        v_stack_m40 = a2;
        result = (unsigned __int16)((result) >> (1));
        a2 = v_rip - 8763610;
        v_stack_m68 = (unsigned __int16)(result);
        result = v_stack_m68;
        v_stack_m58 = result;
        result = *(unsigned __int64 *)(a1 + 8);
        a3 = 0;
        v_stack_m48 = result;
        result = v_stack_p10;
        v_stack_m38 = result;
        result = v_stack_p18;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m78 = result;
        v_stack_m50 = 2;
        v_stack_m3C = 0;
        v_stack_m30 = a4;
        v_stack_m20 = a4;
        result = EtwWrite(*(unsigned __int64 *)(v_rip + 6828971), a2, a3, a4);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLogClearAccessBitsEvent(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m3C;
    uint32_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint16_t v_stack_m68;
    uint64_t v_stack_m78;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x58E0D7)) ^ (local_rsp);
    v_stack_m18 = result;
    local_r10 = 0;
    if (*(uint64_t *)(v_rip + 0x6833AB) != 0) {
        Arg2 = *(uint16_t *)(arg1);
        a4 = local_r10 + 4;
        result = (uint16_t)(Arg2);
        v_stack_m40 = Arg2;
        result = (uint16_t)((result) >> (1));
        Arg2 = v_rip - 8763610;
        v_stack_m68 = (uint16_t)(result);
        result = v_stack_m68;
        v_stack_m58 = result;
        result = *(uint64_t *)(arg1 + 0x8);
        Arg3 = 0;
        v_stack_m48 = result;
        result = v_stack_p10;
        v_stack_m38 = result;
        result = v_stack_p18;
        v_stack_m28 = result;
        result = v_stack_m58;
        v_stack_m78 = result;
        v_stack_m50 = 2;
        v_stack_m3C = 0;
        v_stack_m30 = a4;
        v_stack_m20 = a4;
        result = EtwWrite(*(uint64_t *)(v_rip + 0x6833AB), Arg2, Arg3, a4);
    }
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0087C64C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0087C64C[BB_0087C64C]
  bb_0087C682[BB_0087C682]
  bb_0087C6E3[BB_0087C6E3]
  bb_0087C6F8[BB_0087C6F8]
  bb_0087C64C -->|branch| bb_0087C6E3
  bb_0087C64C -->|fallthrough| bb_0087C682
  bb_0087C682 -->|flow| bb_0087C6E3
```
