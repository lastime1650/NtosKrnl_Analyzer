# KiVerifyXcpt9$fin$2

- RVA: `0x00C8039F`–`0x00C803E0` (길이 `65` bytes)
- VA: `0x0000000140C8039F`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `23`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C803CA` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C803BF` → RVA `0x00C3ADC1` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C803CA` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C8039F  40 55                           push rbp
00C803A1  48 83 EC 20                     sub rsp, 0x20
00C803A5  48 8B EA                        mov rbp, rdx
00C803A8  84 C9                           test cl, cl
00C803AA  74 2D                           je 0x140c803d9
00C803AC  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
00C803B0  83 7A 0C 28                     cmp dword ptr [rdx + 0xc], 0x28
00C803B4  75 1A                           jne 0x140c803d0
00C803B6  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
00C803B9  83 C0 0A                        add eax, 0xa
00C803BC  89 42 0C                        mov dword ptr [rdx + 0xc], eax
00C803BF  48 8D 15 FB A9 FB FF            lea rdx, [rip - 0x45605]
00C803C6  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00C803CA  E8 71 F7 87 FF                  call 0x1404ffb40
00C803CF  90                              nop
00C803D0  48 8B 02                        mov rax, qword ptr [rdx]
00C803D3  8B 08                           mov ecx, dword ptr [rax]
00C803D5  FF C1                           inc ecx
00C803D7  89 08                           mov dword ptr [rax], ecx
00C803D9  48 83 C4 20                     add rsp, 0x20
00C803DD  5D                              pop rbp
00C803DE  C3                              ret
00C803DF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcpt9_fin_2(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a1 == 0) goto loc_00C803D9;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12)) == 40) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12);
        result = (unsigned int)((result) + (10));
        *(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12) = (unsigned int)(result);
        a2 = v_rip - 284165;
        a1 = *(unsigned __int64 *)(a2 + 32);
        result = local_unwind(a1, a2, a3, a4);
    }
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a2)) = a1;
loc_00C803D9:
    v_rsp = (v_rsp) + (32);
    return *(unsigned __int64 *)(a2);
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcpt9_fin_2(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg1 == 0) goto loc_00C803D9;
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC)) == 40) {
        result = *(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC);
        result = (uint32_t)((result) + (10));
        *(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC) = (uint32_t)(result);
        Arg2 = v_rip - 284165;
        Arg1 = *(uint64_t *)(arg2 + 0x20);
        result = local_unwind(Arg1, Arg2, a3, a4);
    }
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2)))) + 1);
    *(uint32_t *)(*(uint64_t *)(arg2)) = Arg1;
loc_00C803D9:
    local_rsp = (local_rsp) + (32);
    return *(uint64_t *)(arg2);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C8039F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C8039F[BB_00C8039F]
  bb_00C803AC[BB_00C803AC]
  bb_00C803B6[BB_00C803B6]
  bb_00C803D0[BB_00C803D0]
  bb_00C803D9[BB_00C803D9]
  bb_00C803DF[BB_00C803DF]
  bb_00C8039F -->|branch| bb_00C803D9
  bb_00C8039F -->|fallthrough| bb_00C803AC
  bb_00C803AC -->|branch| bb_00C803D0
  bb_00C803AC -->|fallthrough| bb_00C803B6
  bb_00C803B6 -->|flow| bb_00C803D0
  bb_00C803D0 -->|flow| bb_00C803D9
```
