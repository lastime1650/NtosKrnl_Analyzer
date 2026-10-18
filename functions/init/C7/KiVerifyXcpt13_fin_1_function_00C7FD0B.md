# KiVerifyXcpt13$fin$1

- RVA: `0x00C7FD0B`–`0x00C7FD3D` (길이 `50` bytes)
- VA: `0x0000000140C7FD0B`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `17`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C7FD30` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C7FD25` → RVA `0x00C3AAA0` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C7FD30` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C7FD0B  40 55                           push rbp
00C7FD0D  48 83 EC 20                     sub rsp, 0x20
00C7FD11  48 8B EA                        mov rbp, rdx
00C7FD14  84 C9                           test cl, cl
00C7FD16  74 1E                           je 0x140c7fd36
00C7FD18  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00C7FD1C  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00C7FD1F  83 C0 0E                        add eax, 0xe
00C7FD22  89 41 0C                        mov dword ptr [rcx + 0xc], eax
00C7FD25  48 8D 15 74 AD FB FF            lea rdx, [rip - 0x4528c]
00C7FD2C  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00C7FD30  E8 0B FE 87 FF                  call 0x1404ffb40
00C7FD35  90                              nop
00C7FD36  48 83 C4 20                     add rsp, 0x20
00C7FD3A  5D                              pop rbp
00C7FD3B  C3                              ret
00C7FD3C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcpt13_fin_1(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a1 != 0) {
        a1 = *(unsigned __int64 *)(a2 + 64);
        result = *(unsigned int *)(a1 + 12);
        result = (unsigned int)((result) + (14));
        *(unsigned int *)(a1 + 12) = (unsigned int)(result);
        a2 = v_rip - 283276;
        a1 = *(unsigned __int64 *)(a2 + 32);
        result = local_unwind(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcpt13_fin_1(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg1 != 0) {
        Arg1 = *(uint64_t *)(arg2 + 0x40);
        result = *(uint32_t *)(Arg1 + 0xC);
        result = (uint32_t)((result) + (14));
        *(uint32_t *)(Arg1 + 0xC) = (uint32_t)(result);
        Arg2 = v_rip - 283276;
        Arg1 = *(uint64_t *)(arg2 + 0x20);
        result = local_unwind(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C7FD0B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C7FD0B[BB_00C7FD0B]
  bb_00C7FD18[BB_00C7FD18]
  bb_00C7FD36[BB_00C7FD36]
  bb_00C7FD3C[BB_00C7FD3C]
  bb_00C7FD0B -->|branch| bb_00C7FD36
  bb_00C7FD0B -->|fallthrough| bb_00C7FD18
  bb_00C7FD18 -->|flow| bb_00C7FD36
```
