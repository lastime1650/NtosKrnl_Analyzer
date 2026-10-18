# IvtLegacyInitializeScalableModePasidTables

- RVA: `0x00571DE4`–`0x00571ED2` (길이 `238` bytes)
- VA: `0x0000000140571DE4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C5160`
- 디코드: `62`개 명령, `238/238` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00571E1B` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00571E2D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00571E7F` → [IvtLegacySetScalableModePasidTableEntry](../4C/IvtLegacySetScalableModePasidTableEntry_function_004CD7CC.md) (function, `0x004CD7CC`)
- `0x00571E97` → [IvtBuildScalableModePasidDirectoryEntry](../4E/IvtBuildScalableModePasidDirectoryEntry_function_004E2D28.md) (function, `0x004E2D28`)
- `0x00571EC1` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [IvtLegacyExtendScalableModePasidTables](IvtLegacyExtendScalableModePasidTables_function_0057134C.md) at `0x005713E5`

### Static image references
- `0x00571DEF` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00571DE4  40 53                           push rbx
00571DE6  56                              push rsi
00571DE7  57                              push rdi
00571DE8  48 81 EC 90 00 00 00            sub rsp, 0x90
00571DEF  48 8B 05 4A 89 89 00            mov rax, qword ptr [rip + 0x89894a]
00571DF6  48 33 C4                        xor rax, rsp
00571DF9  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00571E01  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00571E07  48 8B F2                        mov rsi, rdx
00571E0A  33 D2                           xor edx, edx
00571E0C  41 8B F8                        mov edi, r8d
00571E0F  48 8B D9                        mov rbx, rcx
00571E12  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00571E17  44 8D 42 40                     lea r8d, [rdx + 0x40]
00571E1B  E8 20 4E 15 00                  call 0x1406c6c40
00571E20  48 8B 4C FE 40                  mov rcx, qword ptr [rsi + rdi*8 + 0x40]
00571E25  33 D2                           xor edx, edx
00571E27  41 B8 00 10 00 00               mov r8d, 0x1000
00571E2D  E8 0E 4E 15 00                  call 0x1406c6c40
00571E32  48 8B 43 68                     mov rax, qword ptr [rbx + 0x68]
00571E36  48 85 C0                        test rax, rax
00571E39  74 49                           je 0x140571e84
00571E3B  85 FF                           test edi, edi
00571E3D  75 45                           jne 0x140571e84
00571E3F  48 8B 40 40                     mov rax, qword ptr [rax + 0x40]
00571E43  4C 8D 4C 24 40                  lea r9, [rsp + 0x40]
00571E48  45 33 C0                        xor r8d, r8d
00571E4B  48 8B D6                        mov rdx, rsi
00571E4E  0F 10 40 10                     movups xmm0, xmmword ptr [rax + 0x10]
00571E52  0F 10 10                        movups xmm2, xmmword ptr [rax]
00571E55  0F 10 48 20                     movups xmm1, xmmword ptr [rax + 0x20]
00571E59  0F 29 44 24 50                  movaps xmmword ptr [rsp + 0x50], xmm0
00571E5E  0F 10 40 30                     movups xmm0, xmmword ptr [rax + 0x30]
00571E62  0F 29 54 24 40                  movaps xmmword ptr [rsp + 0x40], xmm2
00571E67  66 48 0F 7E D0                  movq rax, xmm2
00571E6C  48 83 E0 FD                     and rax, 0xfffffffffffffffd
00571E70  0F 29 4C 24 60                  movaps xmmword ptr [rsp + 0x60], xmm1
00571E75  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00571E7A  0F 29 44 24 70                  movaps xmmword ptr [rsp + 0x70], xmm0
00571E7F  E8 48 B9 F5 FF                  call 0x1404cd7cc
00571E84  48 8D 44 24 30                  lea rax, [rsp + 0x30]
00571E89  C1 E7 06                        shl edi, 6
00571E8C  44 8B C7                        mov r8d, edi
00571E8F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00571E94  48 8B D6                        mov rdx, rsi
00571E97  E8 8C 0E F7 FF                  call 0x1404e2d28
00571E9C  48 8B 4E 38                     mov rcx, qword ptr [rsi + 0x38]
00571EA0  8B D7                           mov edx, edi
00571EA2  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00571EA7  90                              nop
00571EA8  48 C1 EA 06                     shr rdx, 6
00571EAC  81 E2 FF 3F 00 00               and edx, 0x3fff
00571EB2  48 89 04 D1                     mov qword ptr [rcx + rdx*8], rax
00571EB6  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00571EBE  48 33 CC                        xor rcx, rsp
00571EC1  E8 7A A7 13 00                  call 0x1406ac640
00571EC6  48 81 C4 90 00 00 00            add rsp, 0x90
00571ECD  5F                              pop rdi
00571ECE  5E                              pop rsi
00571ECF  5B                              pop rbx
00571ED0  C3                              ret
00571ED1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IvtLegacyInitializeScalableModePasidTables(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 9013578)) ^ (v_rsp);
    v_stack_m28 = result;
    a2 = 0;
    result = memset(v_stack_m68, a2, a2 + 64, a4);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(a2 + (unsigned int)(a3) * 8 + 64), a2, (unsigned int)(0x1000ULL), a4);
    if (*(unsigned __int64 *)(a1 + 104) == 0) goto loc_00571E84;
    result = *(unsigned __int64 *)(a1 + 104);
    if ((unsigned int)((unsigned int)(a3)) == 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 104) + 64);
        a4 = v_stack_m68;
        a3 = 0;
        a2 = 0;
        v_stack_m58 = v_xmm0;
        v_stack_m68 = v_xmm2;
        result = (result) & (-3);
        v_stack_m48 = v_xmm1;
        v_stack_m68 = result;
        v_stack_m38 = v_xmm0;
        result = IvtLegacySetScalableModePasidTableEntry(*(unsigned __int64 *)(a2 + (unsigned int)(a3) * 8 + 64), a2, a3, a4);
    }
    v_rdi = (unsigned int)(((unsigned int)(a3)) << (6));
    v_stack_m88 = v_stack_m78;
    result = IvtBuildScalableModePasidDirectoryEntry(*(unsigned __int64 *)(a2 + (unsigned int)(a3) * 8 + 64), a2, (unsigned int)((unsigned int)(v_rdi)), a4);
    a2 = ((unsigned int)((unsigned int)(v_rdi))) >> (6);
    a2 = (unsigned int)((a2) & (0x3FFFULL));
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56) + a2 * 8) = v_stack_m78;
    a1 = (v_stack_m28) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)(v_rdi)), a4);
    v_rsp = (v_rsp) + (144);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IvtLegacyInitializeScalableModePasidTables(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x89894A)) ^ (local_rsp);
    v_stack_m28 = result;
    Arg2 = 0;
    result = memset(v_stack_m68, Arg2, Arg2 + 64, a4);
    Arg2 = 0;
    result = memset(*(uint64_t *)(arg2 + (uint32_t)(Arg3) * 8 + 0x40), Arg2, (uint32_t)(0x1000ULL), a4);
    if (*(uint64_t *)(arg1 + 0x68) == 0) goto loc_00571E84;
    result = *(uint64_t *)(arg1 + 0x68);
    if ((uint32_t)((uint32_t)(Arg3)) == 0) {
        result = *(uint64_t *)(*(uint64_t *)(arg1 + 0x68) + 0x40);
        a4 = v_stack_m68;
        Arg3 = 0;
        Arg2 = 0;
        v_stack_m58 = v_xmm0;
        v_stack_m68 = v_xmm2;
        result = (result) & (-3);
        v_stack_m48 = v_xmm1;
        v_stack_m68 = result;
        v_stack_m38 = v_xmm0;
        result = IvtLegacySetScalableModePasidTableEntry(*(uint64_t *)(arg2 + (uint32_t)(Arg3) * 8 + 0x40), Arg2, Arg3, a4);
    }
    local_rdi = (uint32_t)(((uint32_t)(Arg3)) << (6));
    v_stack_m88 = v_stack_m78;
    result = IvtBuildScalableModePasidDirectoryEntry(*(uint64_t *)(arg2 + (uint32_t)(Arg3) * 8 + 0x40), Arg2, (uint32_t)((uint32_t)(local_rdi)), a4);
    Arg2 = ((uint32_t)((uint32_t)(local_rdi))) >> (6);
    Arg2 = (uint32_t)((Arg2) & (0x3FFFULL));
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x38) + arg2 * 8) = v_stack_m78;
    Arg1 = (v_stack_m28) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)(local_rdi)), a4);
    local_rsp = (local_rsp) + (144);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x40 + rdi*8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00571DE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00571DE4[BB_00571DE4]
  bb_00571E3B[BB_00571E3B]
  bb_00571E3F[BB_00571E3F]
  bb_00571E84[BB_00571E84]
  bb_00571ED1[BB_00571ED1]
  bb_00571DE4 -->|branch| bb_00571E84
  bb_00571DE4 -->|fallthrough| bb_00571E3B
  bb_00571E3B -->|branch| bb_00571E84
  bb_00571E3B -->|fallthrough| bb_00571E3F
  bb_00571E3F -->|flow| bb_00571E84
```
