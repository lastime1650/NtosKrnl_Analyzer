# MiCreatePteWsle

- RVA: `0x00673D00`–`0x00673D3A` (길이 `58` bytes)
- VA: `0x0000000140673D00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00673D2D` → [MiWriteWsle](../29/MiWriteWsle_function_00292CA0.md) (function, `0x00292CA0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00673D00  48 83 EC 28                     sub rsp, 0x28
00673D04  41 83 F8 01                     cmp r8d, 1
00673D08  7D 28                           jge 0x140673d32
00673D0A  48 8B 02                        mov rax, qword ptr [rdx]
00673D0D  A8 01                           test al, 1
00673D0F  74 21                           je 0x140673d32
00673D11  48 C1 E2 19                     shl rdx, 0x19
00673D15  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00673D1F  48 C1 E0 19                     shl rax, 0x19
00673D23  41 B0 09                        mov r8b, 9
00673D26  48 2B D0                        sub rdx, rax
00673D29  48 C1 FA 10                     sar rdx, 0x10
00673D2D  E8 6E EF C1 FF                  call 0x140292ca0
00673D32  33 C0                           xor eax, eax
00673D34  48 83 C4 28                     add rsp, 0x28
00673D38  C3                              ret
00673D39  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCreatePteWsle(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 >= 1) goto loc_00673D32;
    result = *(unsigned __int64 *)(a2);
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2))) & (1)) != 0) {
        a2 = (a2) << (25);
        result = (*(unsigned __int64 *)(a2)) << (25);
        a3 = 9;
        a2 = (a2) - (result);
        a2 = (a2) >> (16);
        result = MiWriteWsle(a1, a2, a3, a4);
    }
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiCreatePteWsle(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 >= 1) goto loc_00673D32;
    result = *(uint64_t *)(arg2);
    if ((((uint8_t)(*(uint64_t *)(arg2))) & (1)) != 0) {
        Arg2 = (Arg2) << (25);
        result = (*(uint64_t *)(arg2)) << (25);
        Arg3 = 9;
        Arg2 = (Arg2) - (result);
        Arg2 = (Arg2) >> (16);
        result = MiWriteWsle(Arg1, Arg2, Arg3, a4);
    }
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00673D00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00673D00[BB_00673D00]
  bb_00673D0A[BB_00673D0A]
  bb_00673D11[BB_00673D11]
  bb_00673D32[BB_00673D32]
  bb_00673D39[BB_00673D39]
  bb_00673D00 -->|branch| bb_00673D32
  bb_00673D00 -->|fallthrough| bb_00673D0A
  bb_00673D0A -->|branch| bb_00673D32
  bb_00673D0A -->|fallthrough| bb_00673D11
  bb_00673D11 -->|flow| bb_00673D32
```
