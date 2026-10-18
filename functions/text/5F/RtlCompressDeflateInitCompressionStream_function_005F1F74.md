# RtlCompressDeflateInitCompressionStream

- RVA: `0x005F1F74`–`0x005F20D5` (길이 `353` bytes)
- VA: `0x00000001405F1F74`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B515C`
- 디코드: `71`개 명령, `353/353` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x005F1FA9` → [AlignWorkspace](AlignWorkspace_function_005F1F58.md) (function, `0x005F1F58`)
- `0x005F202B` → [AlignWorkspace](AlignWorkspace_function_005F1F58.md) (function, `0x005F1F58`)
- `0x005F2046` → [AlignWorkspace](AlignWorkspace_function_005F1F58.md) (function, `0x005F1F58`)
- `0x005F2061` → [AlignWorkspace](AlignWorkspace_function_005F1F58.md) (function, `0x005F1F58`)
- `0x005F20C9` → [deflateReset](deflateReset_function_005F38FC.md) (function, `0x005F38FC`)

### Direct callers
- [RtlCompressBufferDeflateInternal](RtlCompressBufferDeflateInternal_function_005F0694.md) at `0x005F072B`

### Static image references
- `0x005F1F7D` → RVA `0x0048FDC0` (`HalAdjustResourceList`; read)
- `0x005F1F8F` → RVA `0x0049E550` (`EmpCheckErrataList`; read)
- `0x005F2074` → RVA `0x00E67B40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F1F74  40 55                           push rbp
005F1F76  48 8B EC                        mov rbp, rsp
005F1F79  48 83 EC 20                     sub rsp, 0x20
005F1F7D  48 8D 05 3C DE E9 FF            lea rax, [rip - 0x1621c4]
005F1F84  4C 89 49 28                     mov qword ptr [rcx + 0x28], r9
005F1F88  48 89 41 30                     mov qword ptr [rcx + 0x30], rax
005F1F8C  4C 8B D1                        mov r10, rcx
005F1F8F  48 8D 05 BA C5 EA FF            lea rax, [rip - 0x153a46]
005F1F96  48 89 41 38                     mov qword ptr [rcx + 0x38], rax
005F1F9A  49 8D 81 70 17 00 00            lea rax, [r9 + 0x1770]
005F1FA1  48 8D 4D 28                     lea rcx, [rbp + 0x28]
005F1FA5  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
005F1FA9  E8 AA FF FF FF                  call 0x1405f1f58
005F1FAE  45 33 DB                        xor r11d, r11d
005F1FB1  4D 89 11                        mov qword ptr [r9], r10
005F1FB4  41 8B C3                        mov eax, r11d
005F1FB7  41 C7 41 08 2A 00 00 00         mov dword ptr [r9 + 8], 0x2a
005F1FBF  B9 00 80 00 00                  mov ecx, 0x8000
005F1FC4  41 80 F8 01                     cmp r8b, 1
005F1FC8  0F 94 C0                        sete al
005F1FCB  45 8D 43 0F                     lea r8d, [r11 + 0xf]
005F1FCF  41 89 41 2C                     mov dword ptr [r9 + 0x2c], eax
005F1FD3  8D 41 FF                        lea eax, [rcx - 1]
005F1FD6  45 89 81 98 00 00 00            mov dword ptr [r9 + 0x98], r8d
005F1FDD  41 89 81 9C 00 00 00            mov dword ptr [r9 + 0x9c], eax
005F1FE4  41 89 81 CC 00 00 00            mov dword ptr [r9 + 0xcc], eax
005F1FEB  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
005F1FEF  49 89 81 A0 00 00 00            mov qword ptr [r9 + 0xa0], rax
005F1FF6  45 89 81 C8 00 00 00            mov dword ptr [r9 + 0xc8], r8d
005F1FFD  41 B8 00 00 01 00               mov r8d, 0x10000
005F2003  49 03 C0                        add rax, r8
005F2006  41 89 89 94 00 00 00            mov dword ptr [r9 + 0x94], ecx
005F200D  41 89 89 C4 00 00 00            mov dword ptr [r9 + 0xc4], ecx
005F2014  48 8D 4D 28                     lea rcx, [rbp + 0x28]
005F2018  48 89 45 28                     mov qword ptr [rbp + 0x28], rax
005F201C  4D 89 59 30                     mov qword ptr [r9 + 0x30], r11
005F2020  41 C7 81 D0 00 00 00 05 00 00 00  mov dword ptr [r9 + 0xd0], 5
005F202B  E8 28 FF FF FF                  call 0x1405f1f58
005F2030  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
005F2034  49 89 89 B0 00 00 00            mov qword ptr [r9 + 0xb0], rcx
005F203B  49 03 C8                        add rcx, r8
005F203E  48 89 4D 28                     mov qword ptr [rbp + 0x28], rcx
005F2042  48 8D 4D 28                     lea rcx, [rbp + 0x28]
005F2046  E8 0D FF FF FF                  call 0x1405f1f58
005F204B  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
005F204F  49 89 89 B8 00 00 00            mov qword ptr [r9 + 0xb8], rcx
005F2056  49 03 C8                        add rcx, r8
005F2059  48 89 4D 28                     mov qword ptr [rbp + 0x28], rcx
005F205D  48 8D 4D 28                     lea rcx, [rbp + 0x28]
005F2061  E8 F2 FE FF FF                  call 0x1405f1f58
005F2066  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
005F206A  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
005F206E  48 05 00 40 00 00               add rax, 0x4000
005F2074  44 39 1D C5 5A 87 00            cmp dword ptr [rip + 0x875ac5], r11d
005F207B  45 89 99 64 17 00 00            mov dword ptr [r9 + 0x1764], r11d
005F2082  41 C7 81 40 17 00 00 00 40 00 00  mov dword ptr [r9 + 0x1740], 0x4000
005F208D  45 89 41 18                     mov dword ptr [r9 + 0x18], r8d
005F2091  49 89 81 38 17 00 00            mov qword ptr [r9 + 0x1738], rax
005F2098  41 C7 81 48 17 00 00 FD BF 00 00  mov dword ptr [r9 + 0x1748], 0xbffd
005F20A3  41 89 91 FC 00 00 00            mov dword ptr [r9 + 0xfc], edx
005F20AA  45 89 99 00 01 00 00            mov dword ptr [r9 + 0x100], r11d
005F20B1  41 C6 41 3C 08                  mov byte ptr [r9 + 0x3c], 8
005F20B6  74 0E                           je 0x1405f20c6
005F20B8  49 8B 42 28                     mov rax, qword ptr [r10 + 0x28]
005F20BC  C7 80 68 17 00 00 01 00 00 00   mov dword ptr [rax + 0x1768], 1
005F20C6  49 8B CA                        mov rcx, r10
005F20C9  E8 2E 18 00 00                  call 0x1405f38fc
005F20CE  48 83 C4 20                     add rsp, 0x20
005F20D2  5D                              pop rbp
005F20D3  C3                              ret
005F20D4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlCompressDeflateInitCompressionStream(__int64 a1, int a2, unsigned __int8 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;

    v_rsp = (v_rsp) - (32);
    *(unsigned __int64 *)(a1 + 40) = a4;
    *(unsigned __int64 *)(a1 + 48) = v_rip - 1450436;
    *(unsigned __int64 *)(a1 + 56) = v_rip - 1391174;
    v_stack_p20 = a4 + 6000;
    result = AlignWorkspace(v_stack_p20, a2, a3, a4);
    v_r11 = 0;
    *(unsigned __int64 *)(a4) = a1;
    *(unsigned int *)(a4 + 8) = 42;
    result = (a3 == 1) ? 1 : 0;
    *(unsigned int *)(a4 + 44) = (unsigned int)(result);
    *(unsigned int *)(a4 + 152) = (unsigned int)(v_r11 + 15);
    *(unsigned int *)(a4 + 156) = (unsigned int)((unsigned int)(0x8000ULL) - 1);
    *(unsigned int *)(a4 + 204) = (unsigned int)((unsigned int)(0x8000ULL) - 1);
    *(unsigned __int64 *)(a4 + 160) = v_stack_p20;
    *(unsigned int *)(a4 + 200) = (unsigned int)(v_r11 + 15);
    result = (v_stack_p20) + ((unsigned int)(0x10000ULL));
    *(unsigned int *)(a4 + 148) = (unsigned int)((unsigned int)(0x8000ULL));
    *(unsigned int *)(a4 + 196) = (unsigned int)((unsigned int)(0x8000ULL));
    v_stack_p20 = result;
    *(unsigned __int64 *)(a4 + 48) = 0;
    *(unsigned int *)(a4 + 208) = 5;
    result = AlignWorkspace(v_stack_p20, a2, (unsigned int)(0x10000ULL), a4);
    *(unsigned __int64 *)(a4 + 176) = v_stack_p20;
    a1 = (v_stack_p20) + ((unsigned int)(0x10000ULL));
    v_stack_p20 = a1;
    result = AlignWorkspace(v_stack_p20, a2, (unsigned int)(0x10000ULL), a4);
    *(unsigned __int64 *)(a4 + 184) = v_stack_p20;
    a1 = (v_stack_p20) + ((unsigned int)(0x10000ULL));
    v_stack_p20 = a1;
    result = AlignWorkspace(v_stack_p20, a2, (unsigned int)(0x10000ULL), a4);
    *(unsigned __int64 *)(a4 + 16) = v_stack_p20;
    result = (v_stack_p20) + (0x4000ULL);
    *(unsigned int *)(a4 + 5988) = 0;
    *(unsigned int *)(a4 + 5952) = 0x4000ULL;
    *(unsigned int *)(a4 + 24) = (unsigned int)((unsigned int)(0x10000ULL));
    *(unsigned __int64 *)(a4 + 5944) = result;
    *(unsigned int *)(a4 + 5960) = 0xBFFDULL;
    *(unsigned int *)(a4 + 252) = a2;
    *(unsigned int *)(a4 + 256) = 0;
    *(unsigned __int8 *)(a4 + 60) = 8;
    if ((*(unsigned int *)(v_rip + 8870597)) != 0) {
        result = *(unsigned __int64 *)(a1 + 40);
        *(unsigned int *)(result + 5992) = 1;
    }
    result = deflateReset(a1, a2, (unsigned int)(0x10000ULL), a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlCompressDeflateInitCompressionStream(void *Arg1, int32_t Arg2, uint8_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r11;
    int64_t local_rsp;
    uint64_t v_stack_p20;

    local_rsp = (local_rsp) - (32);
    *(void **)(arg1 + 0x28) = Arg4;
    *(uint64_t *)(arg1 + 0x30) = v_rip - 1450436;
    *(uint64_t *)(arg1 + 0x38) = v_rip - 1391174;
    v_stack_p20 = Arg4 + 6000;
    result = AlignWorkspace(v_stack_p20, Arg2, Arg3, Arg4);
    local_r11 = 0;
    *(void **)(arg4) = Arg1;
    *(uint32_t *)(arg4 + 0x8) = 42;
    result = (Arg3 == 1) ? 1 : 0;
    *(uint32_t *)(arg4 + 0x2C) = (uint32_t)(result);
    *(uint32_t *)(arg4 + 0x98) = (uint32_t)(local_r11 + 15);
    *(uint32_t *)(arg4 + 0x9C) = (uint32_t)((uint32_t)(0x8000ULL) - 1);
    *(uint32_t *)(arg4 + 0xCC) = (uint32_t)((uint32_t)(0x8000ULL) - 1);
    *(uint64_t *)(arg4 + 0xA0) = v_stack_p20;
    *(uint32_t *)(arg4 + 0xC8) = (uint32_t)(local_r11 + 15);
    result = (v_stack_p20) + ((uint32_t)(0x10000ULL));
    *(uint32_t *)(arg4 + 0x94) = (uint32_t)((uint32_t)(0x8000ULL));
    *(uint32_t *)(arg4 + 0xC4) = (uint32_t)((uint32_t)(0x8000ULL));
    v_stack_p20 = result;
    *(uint64_t *)(arg4 + 0x30) = 0;
    *(uint32_t *)(arg4 + 0xD0) = 5;
    result = AlignWorkspace(v_stack_p20, Arg2, (uint32_t)(0x10000ULL), Arg4);
    *(uint64_t *)(arg4 + 0xB0) = v_stack_p20;
    Arg1 = (v_stack_p20) + ((uint32_t)(0x10000ULL));
    v_stack_p20 = Arg1;
    result = AlignWorkspace(v_stack_p20, Arg2, (uint32_t)(0x10000ULL), Arg4);
    *(uint64_t *)(arg4 + 0xB8) = v_stack_p20;
    Arg1 = (v_stack_p20) + ((uint32_t)(0x10000ULL));
    v_stack_p20 = Arg1;
    result = AlignWorkspace(v_stack_p20, Arg2, (uint32_t)(0x10000ULL), Arg4);
    *(uint64_t *)(arg4 + 0x10) = v_stack_p20;
    result = (v_stack_p20) + (0x4000ULL);
    *(uint32_t *)(arg4 + 0x1764) = 0;
    *(uint32_t *)(arg4 + 0x1740) = 0x4000ULL;
    *(uint32_t *)(arg4 + 0x18) = (uint32_t)((uint32_t)(0x10000ULL));
    *(uint64_t *)(arg4 + 0x1738) = result;
    *(uint32_t *)(arg4 + 0x1748) = 0xBFFDULL;
    *(uint32_t *)(arg4 + 0xFC) = Arg2;
    *(uint32_t *)(arg4 + 0x100) = 0;
    *(uint8_t *)(arg4 + 0x3C) = 8;
    if ((*(uint32_t *)(v_rip + 0x875AC5)) != 0) {
        result = *(uint64_t *)(arg1 + 0x28);
        *(uint32_t *)(result + 0x1768) = 1;
    }
    result = deflateReset(Arg1, Arg2, (uint32_t)(0x10000ULL), Arg4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `W` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg4` | `+ 0x1770` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F1F74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005F1F74[BB_005F1F74]
  bb_005F20B8[BB_005F20B8]
  bb_005F20C6[BB_005F20C6]
  bb_005F20D4[BB_005F20D4]
  bb_005F1F74 -->|branch| bb_005F20C6
  bb_005F1F74 -->|fallthrough| bb_005F20B8
  bb_005F20B8 -->|flow| bb_005F20C6
```
