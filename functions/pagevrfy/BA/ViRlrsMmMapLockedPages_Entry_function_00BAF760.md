# ViRlrsMmMapLockedPages_Entry

- RVA: `0x00BAF760`–`0x00BAF7AE` (길이 `78` bytes)
- VA: `0x0000000140BAF760`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `20`개 명령, `78/78` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BAF773` → [VfFaultsIsSystemSufficientlyBooted](VfFaultsIsSystemSufficientlyBooted_function_00BA664C.md) (function, `0x00BA664C`)
- `0x00BAF7A3` → [CarReportRuleViolationFromNt](../B9/CarReportRuleViolationFromNt_function_00B9D904.md) (function, `0x00B9D904`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BAF760  48 83 EC 48                     sub rsp, 0x48
00BAF764  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00BAF768  4C 8B D1                        mov r10, rcx
00BAF76B  66 0F BA 60 0A 0D               bt word ptr [rax + 0xa], 0xd
00BAF771  72 35                           jb 0x140baf7a8
00BAF773  E8 D4 6E FF FF                  call 0x140ba664c
00BAF778  85 C0                           test eax, eax
00BAF77A  74 2C                           je 0x140baf7a8
00BAF77C  4D 8B 42 10                     mov r8, qword ptr [r10 + 0x10]
00BAF780  BA 81 00 00 00                  mov edx, 0x81
00BAF785  49 8B 02                        mov rax, qword ptr [r10]
00BAF788  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00BAF78D  C7 44 24 28 02 00 00 00         mov dword ptr [rsp + 0x28], 2
00BAF795  4D 0F BF 48 0A                  movsx r9, word ptr [r8 + 0xa]
00BAF79A  8D 4A 43                        lea ecx, [rdx + 0x43]
00BAF79D  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00BAF7A3  E8 5C E1 FE FF                  call 0x140b9d904
00BAF7A8  48 83 C4 48                     add rsp, 0x48
00BAF7AC  C3                              ret
00BAF7AD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViRlrsMmMapLockedPages_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if (condition_is_below) goto loc_00BAF7A8;
    result = VfFaultsIsSystemSufficientlyBooted(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a3 = *(unsigned __int64 *)(a1 + 16);
        a2 = 129;
        result = *(unsigned __int64 *)(a1);
        v_stack_m18 = result;
        v_stack_m20 = 2;
        a4 = (__int16)(*(unsigned __int16 *)(a3 + 10));
        a1 = a2 + 67;
        result = CarReportRuleViolationFromNt(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViRlrsMmMapLockedPages_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if (condition_is_below) goto loc_00BAF7A8;
    result = VfFaultsIsSystemSufficientlyBooted(Arg1, a2, a3, a4);
    if ((uint32_t)(result) != 0) {
        a3 = *(uint64_t *)(arg1 + 0x10);
        a2 = 129;
        result = *(uint64_t *)(arg1);
        v_stack_m18 = result;
        v_stack_m20 = 2;
        a4 = (int16_t)(*(uint16_t *)(a3 + 0xA));
        Arg1 = a2 + 67;
        result = CarReportRuleViolationFromNt(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BAF760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BAF760[BB_00BAF760]
  bb_00BAF773[BB_00BAF773]
  bb_00BAF77C[BB_00BAF77C]
  bb_00BAF7A8[BB_00BAF7A8]
  bb_00BAF7AD[BB_00BAF7AD]
  bb_00BAF760 -->|branch| bb_00BAF7A8
  bb_00BAF760 -->|fallthrough| bb_00BAF773
  bb_00BAF773 -->|branch| bb_00BAF7A8
  bb_00BAF773 -->|fallthrough| bb_00BAF77C
  bb_00BAF77C -->|flow| bb_00BAF7A8
```
