# MiCopySinglePage$filt$0

- RVA: `0x006D1CD6`–`0x006D1D54` (길이 `126` bytes)
- VA: `0x00000001406D1CD6`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0005FCD8`
- 디코드: `32`개 명령, `126/126` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006D1D3D` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006D1D0F` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D1CD6  40 55                           push rbp
006D1CD8  48 83 EC 30                     sub rsp, 0x30
006D1CDC  48 8B EA                        mov rbp, rdx
006D1CDF  48 89 4D 60                     mov qword ptr [rbp + 0x60], rcx
006D1CE3  48 89 4D 40                     mov qword ptr [rbp + 0x40], rcx
006D1CE7  C7 45 30 00 00 00 00            mov dword ptr [rbp + 0x30], 0
006D1CEE  48 C7 45 48 00 00 00 00         mov qword ptr [rbp + 0x48], 0
006D1CF6  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
006D1CFA  48 8B 08                        mov rcx, qword ptr [rax]
006D1CFD  48 89 4D 48                     mov qword ptr [rbp + 0x48], rcx
006D1D01  C7 45 30 00 00 00 00            mov dword ptr [rbp + 0x30], 0
006D1D08  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D1D0B  85 C0                           test eax, eax
006D1D0D  75 34                           jne 0x1406d1d43
006D1D0F  48 8B 15 72 4D 8F 00            mov rdx, qword ptr [rip + 0x8f4d72]
006D1D16  48 C1 EA 0C                     shr rdx, 0xc
006D1D1A  83 E2 01                        and edx, 1
006D1D1D  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
006D1D21  48 8B 08                        mov rcx, qword ptr [rax]
006D1D24  4C 63 09                        movsxd r9, dword ptr [rcx]
006D1D27  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
006D1D2C  4C 8B 85 A8 00 00 00            mov r8, qword ptr [rbp + 0xa8]
006D1D33  BA 00 50 04 00                  mov edx, 0x45000
006D1D38  B9 1A 00 00 00                  mov ecx, 0x1a
006D1D3D  E8 1E B9 E2 FF                  call 0x1404fd660
006D1D42  90                              nop
006D1D43  C7 45 34 01 00 00 00            mov dword ptr [rbp + 0x34], 1
006D1D4A  8B 45 34                        mov eax, dword ptr [rbp + 0x34]
006D1D4D  48 83 C4 30                     add rsp, 0x30
006D1D51  5D                              pop rbp
006D1D52  C3                              ret
006D1D53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCopySinglePage_filt_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(a2 + 96) = a1;
    *(unsigned __int64 *)(a2 + 64) = a1;
    *(unsigned int *)(a2 + 48) = 0;
    *(unsigned __int64 *)(a2 + 72) = 0;
    *(unsigned __int64 *)(a2 + 72) = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 64));
    *(unsigned int *)(a2 + 48) = 0;
    result = (unsigned int)(*(unsigned int *)(a2 + 48));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48))) == 0) {
        a2 = *(unsigned __int64 *)(v_rip + 9391474);
        a2 = (a2) >> (12);
        a2 = (unsigned int)((a2) & (1));
        result = *(unsigned __int64 *)(a2 + 64);
        a1 = *(unsigned __int64 *)(result);
        a4 = (int)(*(unsigned int *)(a1));
        v_stack_m18 = a2;
        a3 = *(unsigned __int64 *)(a2 + 168);
        a2 = 0x45000ULL;
        a1 = 26;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned int *)(a2 + 52) = 1;
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(*(unsigned int *)(a2 + 52));
}
```

## 5. (Beta) C Style

```c
int64_t MiCopySinglePage_filt_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(arg2 + 0x60) = Arg1;
    *(uint64_t *)(arg2 + 0x40) = Arg1;
    *(uint32_t *)(arg2 + 0x30) = 0;
    *(uint64_t *)(arg2 + 0x48) = 0;
    *(uint64_t *)(arg2 + 0x48) = *(uint64_t *)(*(uint64_t *)(arg2 + 0x40));
    *(uint32_t *)(arg2 + 0x30) = 0;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x30));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30))) == 0) {
        Arg2 = *(uint64_t *)(v_rip + 0x8F4D72);
        Arg2 = (Arg2) >> (12);
        Arg2 = (uint32_t)((Arg2) & (1));
        result = *(uint64_t *)(arg2 + 0x40);
        Arg1 = *(uint64_t *)(result);
        a4 = (int32_t)(*(uint32_t *)(Arg1));
        v_stack_m18 = Arg2;
        a3 = *(uint64_t *)(arg2 + 0xA8);
        Arg2 = 0x45000ULL;
        Arg1 = 26;
        result = KeBugCheckEx(Arg1, Arg2, a3, a4);
    }
    *(uint32_t *)(arg2 + 0x34) = 1;
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(*(uint32_t *)(arg2 + 0x34));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x34` | `32` | `R` |
| `Arg2` | `+ 0x34` | `32` | `W` |
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x40` | `64` | `W` |
| `Arg2` | `+ 0x48` | `64` | `W` |
| `Arg2` | `+ 0x60` | `64` | `W` |
| `Arg2` | `+ 0xA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D1CD6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D1CD6[BB_006D1CD6]
  bb_006D1D0F[BB_006D1D0F]
  bb_006D1D43[BB_006D1D43]
  bb_006D1D53[BB_006D1D53]
  bb_006D1CD6 -->|branch| bb_006D1D43
  bb_006D1CD6 -->|fallthrough| bb_006D1D0F
  bb_006D1D0F -->|flow| bb_006D1D43
```
