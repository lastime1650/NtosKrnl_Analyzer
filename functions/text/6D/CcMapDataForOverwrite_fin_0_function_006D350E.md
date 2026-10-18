# CcMapDataForOverwrite$fin$0

- RVA: `0x006D350E`–`0x006D3559` (길이 `75` bytes)
- VA: `0x00000001406D350E`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AAC90`
- 디코드: `23`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006D354C` → [CcUnpinFileDataEx](../35/CcUnpinFileDataEx_function_00359DEC.md) (function, `0x00359DEC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D350E  40 55                           push rbp
006D3510  48 83 EC 30                     sub rsp, 0x30
006D3514  48 8B EA                        mov rbp, rdx
006D3517  44 8B 85 A0 00 00 00            mov r8d, dword ptr [rbp + 0xa0]
006D351E  41 8A C0                        mov al, r8b
006D3521  24 01                           and al, 1
006D3523  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
006D3527  88 82 AC 05 00 00               mov byte ptr [rdx + 0x5ac], al
006D352D  41 D1 E8                        shr r8d, 1
006D3530  44 89 82 98 05 00 00            mov dword ptr [rdx + 0x598], r8d
006D3537  84 C9                           test cl, cl
006D3539  74 17                           je 0x1406d3552
006D353B  48 8B 8D A8 00 00 00            mov rcx, qword ptr [rbp + 0xa8]
006D3542  48 85 C9                        test rcx, rcx
006D3545  74 0B                           je 0x1406d3552
006D3547  45 33 C0                        xor r8d, r8d
006D354A  33 D2                           xor edx, edx
006D354C  E8 9B 68 C8 FF                  call 0x140359dec
006D3551  90                              nop
006D3552  48 83 C4 30                     add rsp, 0x30
006D3556  5D                              pop rbp
006D3557  C3                              ret
006D3558  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcMapDataForOverwrite_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 160)))) & (1));
    *(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 64) + 1452) = (unsigned __int8)(result);
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 160))) >> (1));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 1432) = (unsigned int)(a3);
    if (a1 == 0) goto loc_006D3552;
    if (*(unsigned __int64 *)(a2 + 168) != 0) {
        a3 = 0;
        a2 = 0;
        result = CcUnpinFileDataEx(*(unsigned __int64 *)(a2 + 168), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcMapDataForOverwrite_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    result = (uint8_t)(((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0xA0)))) & (1));
    *(uint8_t *)(*(uint64_t *)(arg2 + 0x40) + 0x5AC) = (uint8_t)(result);
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0xA0))) >> (1));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0x598) = (uint32_t)(a3);
    if (Arg1 == 0) goto loc_006D3552;
    if (*(uint64_t *)(arg2 + 0xA8) != 0) {
        a3 = 0;
        Arg2 = 0;
        result = CcUnpinFileDataEx(*(uint64_t *)(arg2 + 0xA8), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0xA0` | `32` | `R` |
| `Arg2` | `+ 0xA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D350E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D350E[BB_006D350E]
  bb_006D353B[BB_006D353B]
  bb_006D3547[BB_006D3547]
  bb_006D3552[BB_006D3552]
  bb_006D3558[BB_006D3558]
  bb_006D350E -->|branch| bb_006D3552
  bb_006D350E -->|fallthrough| bb_006D353B
  bb_006D353B -->|branch| bb_006D3552
  bb_006D353B -->|fallthrough| bb_006D3547
  bb_006D3547 -->|flow| bb_006D3552
```
