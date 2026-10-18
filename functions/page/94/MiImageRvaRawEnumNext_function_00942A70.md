# MiImageRvaRawEnumNext

- RVA: `0x00942A70`–`0x00942A9D` (길이 `45` bytes)
- VA: `0x0000000140942A70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000903F4`
- 디코드: `10`개 명령, `45/45` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00942A8A` → [sub_00942C6B + 0x1](Unknown_function_00942C6B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00942A70  4C 8B DC                        mov r11, rsp
00942A73  53                              push rbx
00942A74  41 55                           push r13
00942A76  48 81 EC 88 00 00 00            sub rsp, 0x88
00942A7D  83 B9 38 01 00 00 00            cmp dword ptr [rcx + 0x138], 0
00942A84  4C 8B EA                        mov r13, rdx
00942A87  48 8B D9                        mov rbx, rcx
00942A8A  0F 84 DC 01 00 00               je 0x140942c6c
00942A90  8B 91 90 00 00 00               mov edx, dword ptr [rcx + 0x90]
00942A96  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiImageRvaRawEnumNext(__int64 a1, __int64 a2)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (136);
    return a1 + 152;
}
```

## 5. (Beta) C Style

```c
void *MiImageRvaRawEnumNext(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (136);
    return Arg1 + 152;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x90` | `32` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0x138` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00942A70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00942A70[BB_00942A70]
  bb_00942A90[BB_00942A90]
  bb_00942A70 -->|fallthrough| bb_00942A90
```
