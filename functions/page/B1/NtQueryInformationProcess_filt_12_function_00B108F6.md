# NtQueryInformationProcess$filt$12

- RVA: `0x00B108F6`–`0x00B10932` (길이 `60` bytes)
- VA: `0x0000000140B108F6`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009DFAC`
- 디코드: `16`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B108F6  40 55                           push rbp
00B108F8  48 83 EC 40                     sub rsp, 0x40
00B108FC  48 8B EA                        mov rbp, rdx
00B108FF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B10908  48 89 85 38 02 00 00            mov qword ptr [rbp + 0x238], rax
00B1090F  48 8B 85 38 02 00 00            mov rax, qword ptr [rbp + 0x238]
00B10916  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
00B1091D  88 4D 72                        mov byte ptr [rbp + 0x72], cl
00B10920  0F B6 4D 72                     movzx ecx, byte ptr [rbp + 0x72]
00B10924  33 C0                           xor eax, eax
00B10926  84 C9                           test cl, cl
00B10928  0F 95 C0                        setne al
00B1092B  48 83 C4 40                     add rsp, 0x40
00B1092F  5D                              pop rbp
00B10930  C3                              ret
00B10931  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryInformationProcess_filt_12(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(a2 + 568) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int8 *)(a2 + 114) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 568) + 562));
    result = 0;
    result = ((unsigned __int8)(*(unsigned __int8 *)(a2 + 114)) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (64);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryInformationProcess_filt_12(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(arg2 + 0x238) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint8_t *)(arg2 + 0x72) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x238) + 0x232));
    result = 0;
    result = ((uint8_t)(*(uint8_t *)(arg2 + 0x72)) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (64);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x72` | `8` | `R` |
| `Arg2` | `+ 0x72` | `8` | `W` |
| `Arg2` | `+ 0x238` | `64` | `R` |
| `Arg2` | `+ 0x238` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B108F6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B108F6[BB_00B108F6]
  bb_00B10931[BB_00B10931]
```
