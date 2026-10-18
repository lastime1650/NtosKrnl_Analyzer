# CcPinRead$fin$0

- RVA: `0x00B132E1`–`0x00B13321` (길이 `64` bytes)
- VA: `0x0000000140B132E1`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B4FD4`
- 디코드: `18`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B13314` → [CcUnpinData](../9A/CcUnpinData_function_009A7A80.md) (function, `0x009A7A80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B132E1  40 55                           push rbp
00B132E3  48 83 EC 50                     sub rsp, 0x50
00B132E7  48 8B EA                        mov rbp, rdx
00B132EA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B132F3  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
00B132F7  8B 80 DC 05 00 00               mov eax, dword ptr [rax + 0x5dc]
00B132FD  65 01 04 25 98 89 00 00         add dword ptr gs:[0x8998], eax
00B13305  80 7D 50 00                     cmp byte ptr [rbp + 0x50], 0
00B13309  75 0F                           jne 0x140b1331a
00B1330B  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
00B1330F  48 85 C9                        test rcx, rcx
00B13312  74 06                           je 0x140b1331a
00B13314  E8 67 47 E9 FF                  call 0x1409a7a80
00B13319  90                              nop
00B1331A  48 83 C4 50                     add rsp, 0x50
00B1331E  5D                              pop rbp
00B1331F  C3                              ret
00B13320  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcPinRead_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (80);
    *(unsigned __int64 *)(a2 + 112) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int8 *)(a2 + 80)) != 0) goto loc_00B1331A;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1500));
    if (*(unsigned __int64 *)(a2 + 88) != 0) {
        result = CcUnpinData(*(unsigned __int64 *)(a2 + 88), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcPinRead_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (80);
    *(uint64_t *)(arg2 + 0x70) = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint8_t *)(arg2 + 0x50)) != 0) goto loc_00B1331A;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5DC));
    if (*(uint64_t *)(arg2 + 0x58) != 0) {
        result = CcUnpinData(*(uint64_t *)(arg2 + 0x58), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x50` | `8` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |
| `Arg2` | `+ 0x70` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B132E1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B132E1[BB_00B132E1]
  bb_00B1330B[BB_00B1330B]
  bb_00B13314[BB_00B13314]
  bb_00B1331A[BB_00B1331A]
  bb_00B13320[BB_00B13320]
  bb_00B132E1 -->|branch| bb_00B1331A
  bb_00B132E1 -->|fallthrough| bb_00B1330B
  bb_00B1330B -->|branch| bb_00B1331A
  bb_00B1330B -->|fallthrough| bb_00B13314
  bb_00B13314 -->|flow| bb_00B1331A
```
