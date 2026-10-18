# sub_0031FD43

- RVA: `0x0031FD43`–`0x0031FD68` (길이 `37` bytes)
- VA: `0x000000014031FD43`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075458`
- 디코드: `8`개 명령, `37/37` bytes 표시
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
  - `0x0031FD62` → [sub_0031FDF6](Unknown_function_0031FDF6.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031FD43  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
0031FD48  0F B6 69 04                     movzx ebp, byte ptr [rcx + 4]
0031FD4C  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
0031FD51  48 8B 71 40                     mov rsi, qword ptr [rcx + 0x40]
0031FD55  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
0031FD5A  33 FF                           xor edi, edi
0031FD5C  39 BE 18 01 00 00               cmp dword ptr [rsi + 0x118], edi
0031FD62  0F 86 8E 00 00 00               jbe 0x14031fdf6
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0031FD43(__int64 a1)
{
    __int64 v_rdi;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;

    v_stack_p50 = v_rbp;
    v_stack_p58 = v_rsi;
    v_stack_p60 = v_rdi;
    v_rdi = 0;
}
```

## 5. (Beta) C Style

```c
void sub_0031FD43(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rdi;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;

    v_stack_p50 = local_rbp;
    v_stack_p58 = local_rsi;
    v_stack_p60 = local_rdi;
    local_rdi = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `8` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031FD43&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031FD43[BB_0031FD43]
```
