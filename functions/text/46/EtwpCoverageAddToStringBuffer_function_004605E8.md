# EtwpCoverageAddToStringBuffer

- RVA: `0x004605E8`–`0x00460621` (길이 `57` bytes)
- VA: `0x00000001404605E8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `18`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00460609` → [RtlStringCchCopyA](RtlStringCchCopyA_function_00460628.md) (function, `0x00460628`)

### Direct callers
- [EtwTelemetryCoverageReport](EtwTelemetryCoverageReport_function_00460430.md) at `0x00460502`
- [EtwpCoverageRecord](../../page/98/EtwpCoverageRecord_function_009821BC.md) at `0x00982347`
- [sub_00B2A746](../../page/B2/Unknown_function_00B2A746.md) at `0x00B2A752`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004605E8  48 83 EC 28                     sub rsp, 0x28
004605EC  4C 8B D1                        mov r10, rcx
004605EF  45 8D 58 01                     lea r11d, [r8 + 1]
004605F3  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
004605F7  4C 8B CA                        mov r9, rdx
004605FA  49 8B 52 10                     mov rdx, qword ptr [r10 + 0x10]
004605FE  48 2B D1                        sub rdx, rcx
00460601  49 3B D3                        cmp rdx, r11
00460604  72 17                           jb 0x14046061d
00460606  4D 8B C1                        mov r8, r9
00460609  E8 1A 00 00 00                  call 0x140460628
0046060E  4D 01 5A 18                     add qword ptr [r10 + 0x18], r11
00460612  B8 01 00 00 00                  mov eax, 1
00460617  48 83 C4 28                     add rsp, 0x28
0046061B  C3                              ret
0046061C  CC                              int3
0046061D  33 C0                           xor eax, eax
0046061F  EB F6                           jmp 0x140460617
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpCoverageAddToStringBuffer(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (*(unsigned __int64 *)(a1 + 16)) - (*(unsigned __int64 *)(a1 + 24));
    if (a2 < (a3 + 1)) goto loc_0046061D;
    result = RtlStringCchCopyA(*(unsigned __int64 *)(a1 + 24), a2, a2, a2);
loc_00460617:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_0046061D:
    result = 0;
    goto loc_00460617;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpCoverageAddToStringBuffer(void *Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (*(uint64_t *)(arg1 + 0x10)) - (*(uint64_t *)(arg1 + 0x18));
    if (Arg2 < (Arg3 + 1)) goto loc_0046061D;
    result = RtlStringCchCopyA(*(uint64_t *)(arg1 + 0x18), Arg2, Arg2, Arg2);
loc_00460617:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_0046061D:
    result = 0;
    goto loc_00460617;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg3` | `+ 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004605E8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004605E8[BB_004605E8]
  bb_00460606[BB_00460606]
  bb_00460617[BB_00460617]
  bb_0046061C[BB_0046061C]
  bb_0046061D[BB_0046061D]
  bb_004605E8 -->|branch| bb_0046061D
  bb_004605E8 -->|fallthrough| bb_00460606
  bb_00460606 -->|flow| bb_00460617
  bb_0046061C -->|flow| bb_0046061D
  bb_0046061D -->|branch| bb_00460617
```
