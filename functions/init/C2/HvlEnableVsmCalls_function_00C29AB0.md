# HvlEnableVsmCalls

- RVA: `0x00C29AB0`–`0x00C29AE0` (길이 `48` bytes)
- VA: `0x0000000140C29AB0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C29AC7` → [HvlpTryConfigureInterface](../../text/58/HvlpTryConfigureInterface_function_0058CABC.md) (function, `0x0058CABC`)
- `0x00C29AD0` → [HvlpGetVtlCallVa](../../text/58/HvlpGetVtlCallVa_function_0058D560.md) (function, `0x0058D560`)
- `0x00C29AD5` → [VslBindNtIum](VslBindNtIum_function_00C29B74.md) (function, `0x00C29B74`)

### Direct callers
- [KiInitializeBootStructures](../../pagelk/B6/KiInitializeBootStructures_function_00B68530.md) at `0x00B687BD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C29AC7` → [HvlpTryConfigureInterface](../../text/58/HvlpTryConfigureInterface_function_0058CABC.md) (`INIT` → `.text`)
  - `0x00C29AD0` → [HvlpGetVtlCallVa](../../text/58/HvlpGetVtlCallVa_function_0058D560.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C29AB0  48 83 EC 28                     sub rsp, 0x28
00C29AB4  48 8B 81 F0 00 00 00            mov rax, qword ptr [rcx + 0xf0]
00C29ABB  F7 80 84 00 00 00 00 01 00 00   test dword ptr [rax + 0x84], 0x100
00C29AC5  74 13                           je 0x140c29ada
00C29AC7  E8 F0 2F 96 FF                  call 0x14058cabc
00C29ACC  85 C0                           test eax, eax
00C29ACE  78 0A                           js 0x140c29ada
00C29AD0  E8 8B 3A 96 FF                  call 0x14058d560
00C29AD5  E8 9A 00 00 00                  call 0x140c29b74
00C29ADA  48 83 C4 28                     add rsp, 0x28
00C29ADE  C3                              ret
00C29ADF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlEnableVsmCalls(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132)) & (256)) == 0) goto loc_00C29ADA;
    result = HvlpTryConfigureInterface(a1, a2, a3, a4);
    if (!(sign_flag)) {
        result = HvlpGetVtlCallVa(a1, a2, a3, a4);
        result = VslBindNtIum(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlEnableVsmCalls(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x84)) & (256)) == 0) goto loc_00C29ADA;
    result = HvlpTryConfigureInterface(Arg1, a2, a3, a4);
    if (!(sign_flag)) {
        result = HvlpGetVtlCallVa(Arg1, a2, a3, a4);
        result = VslBindNtIum(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C29AB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C29AB0[BB_00C29AB0]
  bb_00C29AC7[BB_00C29AC7]
  bb_00C29AD0[BB_00C29AD0]
  bb_00C29ADA[BB_00C29ADA]
  bb_00C29ADF[BB_00C29ADF]
  bb_00C29AB0 -->|branch| bb_00C29ADA
  bb_00C29AB0 -->|fallthrough| bb_00C29AC7
  bb_00C29AC7 -->|branch| bb_00C29ADA
  bb_00C29AC7 -->|fallthrough| bb_00C29AD0
  bb_00C29AD0 -->|flow| bb_00C29ADA
```
