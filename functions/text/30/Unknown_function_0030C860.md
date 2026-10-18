# sub_0030C860

- RVA: `0x0030C860`–`0x0030C880` (길이 `32` bytes)
- VA: `0x000000014030C860`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00073D94`
- 디코드: `8`개 명령, `32/32` bytes 표시
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
  - `0x0030C87E` → [sub_0030C8FC](Unknown_function_0030C8FC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0030C860  48 8B 81 58 8E 00 00            mov rax, qword ptr [rcx + 0x8e58]
0030C867  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
0030C86B  48 8B CF                        mov rcx, rdi
0030C86E  85 ED                           test ebp, ebp
0030C870  41 88 04 0C                     mov byte ptr [r12 + rcx], al
0030C874  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
0030C879  48 8B 6C 24 60                  mov rbp, qword ptr [rsp + 0x60]
0030C87E  75 7C                           jne 0x14030c8fc
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0030C860(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12)
{
    *(unsigned __int8 *)(v_r12 + v_rdi * 1) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 36440) + 1));
}
```

## 5. (Beta) C Style

```c
int64_t sub_0030C860(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, int64_t Arg11, int64_t Arg12)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint8_t *)(local_r12 + local_rdi * 1) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0x8E58) + 0x1));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8E58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0030C860&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0030C860[BB_0030C860]
```
