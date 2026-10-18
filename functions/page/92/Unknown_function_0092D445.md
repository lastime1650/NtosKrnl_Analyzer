# sub_0092D445

- RVA: `0x0092D445`–`0x0092D4C0` (길이 `123` bytes)
- VA: `0x000000014092D445`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DBA4`
- 디코드: `47`개 명령, `123/123` bytes 표시
- 미해석 바이트: `7` (있으면 어셈블리에 `.byte`로 보존)

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
0092D445  CC                              int3
0092D446  66 90                           nop
0092D448  59                              pop rcx
0092D449  CE                              .byte 0xce
0092D44A  92                              xchg edx, eax
0092D44B  00 59 CE                        add byte ptr [rcx - 0x32], bl
0092D44E  92                              xchg edx, eax
0092D44F  00 8B CE 92 00 8B               add byte ptr [rbx - 0x74ff6d32], cl
0092D455  CE                              .byte 0xce
0092D456  92                              xchg edx, eax
0092D457  00 8B CE 92 00 59               add byte ptr [rbx + 0x590092ce], cl
0092D45D  CE                              .byte 0xce
0092D45E  92                              xchg edx, eax
0092D45F  00 59 CE                        add byte ptr [rcx - 0x32], bl
0092D462  92                              xchg edx, eax
0092D463  00 8B CE 92 00 8B               add byte ptr [rbx - 0x74ff6d32], cl
0092D469  CE                              .byte 0xce
0092D46A  92                              xchg edx, eax
0092D46B  00 8B CE 92 00 8B               add byte ptr [rbx - 0x74ff6d32], cl
0092D471  CE                              .byte 0xce
0092D472  92                              xchg edx, eax
0092D473  00 59 CE                        add byte ptr [rcx - 0x32], bl
0092D476  92                              xchg edx, eax
0092D477  00 59 CE                        add byte ptr [rcx - 0x32], bl
0092D47A  92                              xchg edx, eax
0092D47B  00 59 CE                        add byte ptr [rcx - 0x32], bl
0092D47E  92                              xchg edx, eax
0092D47F  00 59 CE                        add byte ptr [rcx - 0x32], bl
0092D482  92                              xchg edx, eax
0092D483  00 FD                           add ch, bh
0092D485  D1 92 00 FD D1 92               rcl dword ptr [rdx - 0x6d2e0300]
0092D48B  00 19                           add byte ptr [rcx], bl
0092D48D  D2 92 00 19 D2 92               rcl byte ptr [rdx - 0x6d2de700], cl
0092D493  00 19                           add byte ptr [rcx], bl
0092D495  D2 92 00 FD D1 92               rcl byte ptr [rdx - 0x6d2e0300], cl
0092D49B  00 FD                           add ch, bh
0092D49D  D1 92 00 19 D2 92               rcl dword ptr [rdx - 0x6d2de700]
0092D4A3  00 19                           add byte ptr [rcx], bl
0092D4A5  D2 92 00 19 D2 92               rcl byte ptr [rdx - 0x6d2de700], cl
0092D4AB  00 19                           add byte ptr [rcx], bl
0092D4AD  D2 92 00 FD D1 92               rcl byte ptr [rdx - 0x6d2e0300], cl
0092D4B3  00 FD                           add ch, bh
0092D4B5  D1 92 00 FD D1 92               rcl dword ptr [rdx - 0x6d2e0300]
0092D4BB  00 FD                           add ch, bh
0092D4BD  D1                              .byte 0xd1
0092D4BE  92                              xchg edx, eax
0092D4BF  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0092D445(__int64 a1, int a2)
{
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(v_rbx)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(v_rbx)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(v_rbx)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(v_rbx)));
    return;
}
```

## 5. (Beta) C Style

```c
void sub_0092D445(int64_t Arg1, int32_t Arg2)
{
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(local_rbx)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(local_rbx)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(local_rbx)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(local_rbx)));
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092D445&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0092D445[BB_0092D445]
```
